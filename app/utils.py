import jwt
from functools import wraps
from flask import request, jsonify, current_app
from app.models import Profile

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]
            
        if not token:
            return jsonify({"error": "Authentication token is missing!"}), 401
            
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Profile.query.get(data['sub'])
            
            if not current_user or current_user.role != 'admin':
                return jsonify({"error": "Admin privileges required"}), 403
                
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token is invalid!"}), 401
            
        return f(current_user, *args, **kwargs)
        
    return decorated

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').split(" ")[1] if 'Authorization' in request.headers else None
        if not token: return jsonify({"error": "Token missing"}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = Profile.query.get(data['sub'])
            if not current_user: raise Exception()
        except:
            return jsonify({"error": "Invalid or expired token"}), 401
        return f(current_user, *args, **kwargs)
    return decorated