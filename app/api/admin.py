import os
from flask import Blueprint, jsonify, current_app
from app import db
from app.models import Pengaduan
from app.utils import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/reports', methods=['GET'])
@admin_required
def get_all_reports(current_user):
    reports = Pengaduan.query.order_by(Pengaduan.dibuatPada.desc()).all()
    
    return jsonify({
        "reports": [report.to_dict() for report in reports]
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