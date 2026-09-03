import jwt
import datetime
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import Profile

# Initialize the blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Basic validation
    if not data or not data.get('email') or not data.get('password') or not data.get('namaLengkap'):
        return jsonify({"error": "Missing required fields"}), 400
        
    # Check if user already exists
    if Profile.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 409
        
    # Hash the password for secure storage
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    
    # Note: Using your default role logic, though you might want regular users 
    # to be created as "user" instead of "admin" for FixinIT
    new_user = Profile(
        email=data['email'],
        namaLengkap=data['namaLengkap'],
        password_hash=hashed_password,
        role=data.get('role', 'user') 
    )
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        "message": "User registered successfully",
        "user": new_user.to_dict()
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing email or password"}), 400
        
    # Find the user by email
    user = Profile.query.filter_by(email=data['email']).first()
    
    # Verify user exists and password matches the hash
    if not user or not check_password_hash(user.password_hash, data['password']):
        return jsonify({"error": "Invalid email or password"}), 401
        
    # Generate the JWT
    # 'exp' sets expiration (e.g., 24 hours), 'sub' is the subject (user ID)
    token = jwt.encode({
        'sub': user.id,
        'role': user.role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
    }, current_app.config['SECRET_KEY'], algorithm='HS256')
    
    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": user.to_dict()
    }), 200