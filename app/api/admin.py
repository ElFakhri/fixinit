import os
from flask import Blueprint, jsonify, current_app, request
from app import db
from app.models import Pengaduan, Profile
from app.utils import admin_required

admin_bp = Blueprint('admin', __name__)
VALID_REPORT_STATUSES = {"pending", "validated", "rejected"}


def _set_report_status(report_id, status):
    report = Pengaduan.query.get(report_id)
    if not report:
        return None, jsonify({"error": "Report not found"}), 404

    normalized_status = (status or "").strip().lower()
    if normalized_status not in VALID_REPORT_STATUSES:
        allowed = ", ".join(sorted(VALID_REPORT_STATUSES))
        return None, jsonify({"error": f"Invalid status. Allowed: {allowed}"}), 400

    report.status = normalized_status
    db.session.commit()
    return report, None, None


@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_all_users(current_user):
    users = Profile.query.order_by(Profile.dibuatPada.desc()).all()

    return jsonify({
        "users": [user.to_dict() for user in users]
    }), 200


@admin_bp.route('/reports', methods=['GET'])
@admin_required
def get_all_reports(current_user):
    reports = Pengaduan.query.order_by(Pengaduan.dibuatPada.desc()).all()

    return jsonify({
        "reports": [report.to_dict() for report in reports]
    }), 200


@admin_bp.route('/reports/<report_id>/status', methods=['PATCH', 'PUT'])
@admin_required
def update_report_status(current_user, report_id):
    data = request.get_json(silent=True) or {}
    new_status = data.get('status') or request.args.get('status')

    if not new_status:
        return jsonify({"error": "Status is required"}), 400

    report, error_response, status_code = _set_report_status(report_id, new_status)
    if error_response is not None:
        return error_response, status_code

    return jsonify({
        "message": f"Report status updated to {report.status}",
        "report": report.to_dict()
    }), 200


@admin_bp.route('/reports/<report_id>/validate', methods=['PATCH', 'PUT'])
@admin_required
def validate_report(current_user, report_id):
    report, error_response, status_code = _set_report_status(report_id, 'validated')
    if error_response is not None:
        return error_response, status_code

    return jsonify({
        "message": "Report validated successfully",
        "report": report.to_dict()
    }), 200


@admin_bp.route('/reports/<report_id>', methods=['DELETE'])
@admin_required
def delete_report(current_user, report_id):
    report = Pengaduan.query.get(report_id)

    if not report:
        return jsonify({"error": "Report not found"}), 404

    if report.pictureUrl:
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], report.pictureUrl)
        if os.path.exists(file_path):
            os.remove(file_path)

    # Delete the record from the database
    db.session.delete(report)
    db.session.commit()

    return jsonify({
        "message": "Report and associated image deleted successfully",
        "id": report_id
    }), 200