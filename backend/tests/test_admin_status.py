import os
import datetime

import jwt
import pytest

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

from app import create_app, db
from app.models import Pengaduan, Profile
from werkzeug.security import generate_password_hash


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)

    with app.app_context():
        db.drop_all()
        db.create_all()

        admin = Profile(
            email="admin@example.com",
            namaLengkap="Admin User",
            password_hash=generate_password_hash("secret"),
            role="admin",
        )
        db.session.add(admin)
        db.session.commit()

        report = Pengaduan(
            profile_id=admin.id,
            description="Broken pipe",
            lokasi="Jakarta",
            status="pending",
        )
        db.session.add(report)
        db.session.commit()

        token = jwt.encode(
            {
                "sub": admin.id,
                "role": "admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            },
            app.config["SECRET_KEY"],
            algorithm="HS256",
        )

        yield app.test_client(), report.id, token

        db.session.remove()
        db.drop_all()


def test_admin_can_validate_report(client):
    test_client, report_id, token = client

    response = test_client.patch(
        f"/api/admin/reports/{report_id}/validate",
        headers={"Authorization": f"Bearer {token}"},
    )

    assert response.status_code == 200
    assert response.get_json()["report"]["status"] == "validated"


def test_admin_can_update_status_via_generic_endpoint(client):
    test_client, report_id, token = client

    response = test_client.patch(
        f"/api/admin/reports/{report_id}/status",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        json={"status": "rejected"},
    )

    assert response.status_code == 200
    assert response.get_json()["report"]["status"] == "rejected"
