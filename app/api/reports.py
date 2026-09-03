import os
import uuid
from werkzeug.utils import secure_filename
from flask import Blueprint, request, jsonify, current_app, send_from_directory
from app import db
from app.models import Pengaduan
from app.utils import token_required

reports_bp = Blueprint('reports', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@reports_bp.route('/', methods=['POST'])
@token_required
def create_report(current_user):
    # Use request.form instead of request.get_json() for multipart/form-data
    description = request.form.get('description')
    lokasi = request.form.get('lokasi')
    
    if not description or not lokasi:
        return jsonify({"error": "Description and lokasi are required"}), 400
        
    # 2. Extract the uploaded file
    picture_file = request.files.get('picture')
    filename = None
    
    if picture_file:
        if not allowed_file(picture_file.filename):
            return jsonify({"error": "Invalid file type. Allowed: JPG, PNG, WEBP"}), 400
            
        ext = picture_file.filename.rsplit('.', 1)[1].lower()
        
        filename = f"{uuid.uuid4().hex}.{ext}"
        save_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        picture_file.save(save_path)

    new_report = Pengaduan(
        profile_id=current_user.id,
        description=description,
        lokasi=lokasi,
        pictureUrl=filename
    )
    
    db.session.add(new_report)
    db.session.commit()
    
    return jsonify({
        "message": "Pengaduan submitted successfully",
        "report": new_report.to_dict()
    }), 201

@reports_bp.route('/', methods=['GET'])
@token_required
def get_my_reports(current_user):
    reports = Pengaduan.query.filter_by(profile_id=current_user.id).order_by(Pengaduan.dibuatPada.desc()).all()
    
    return jsonify({
        "reports": [report.to_dict() for report in reports]
    }), 200

@reports_bp.route('/images/<filename>', methods=['GET'])
def get_image(filename):
    # This route is critical. When Vue renders <img src="http://localhost:5000/api/reports/images/xyz.jpg">,
    # this function safely serves the file from your protected uploads folder.
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)