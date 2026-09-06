import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app(config_object='app.config.Config'):
    app = Flask(__name__)
    
    app.config.from_object(config_object)
    
    db.init_app(app)
    
    cors.init_app(app, resources={r"/api/*": {"origins": "*"}}) 
    
    os.makedirs(app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)
    
    from app.api.auth import auth_bp
    from app.api.reports import reports_bp
    from app.api.admin import admin_bp
    
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(reports_bp, url_prefix='/api/reports')
    app.register_blueprint(admin_bp, url_prefix='/api/admin')
    
    with app.app_context():
        db.create_all()
        
    return app