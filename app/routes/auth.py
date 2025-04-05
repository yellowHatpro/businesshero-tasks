from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import AuthService

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # validations
    if not data:
        return jsonify({"message": "Invalid request data"}), 400
    
    result, error = auth_service.login(data.get('username'), data.get('password'))
    
    if error:
        return jsonify({"message": error}), 401
    
    if not result:
        return jsonify({"message": "Authentication failed"}), 401
        
    # return response for successful login
    return jsonify({"message": "Login successful", "access_token": result["access_token"]}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "Invalid request data"}), 400
    
    user, error = auth_service.register(
        data.get('username'),
        data.get('email'),
        data.get('password')
    )
    
    if error:
        return jsonify({"message": error}), 400
    
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    current_user_id = get_jwt_identity()
    current_user_id = int(current_user_id)
    profile, error = auth_service.get_user_profile(current_user_id)
    
    if error:
        return jsonify({"message": error}), 404
    
    return jsonify(profile), 200

