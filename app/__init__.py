from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Database configuration
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    
    # JWT configuration
    app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 86400  # 24 hours
    app.config["JWT_ERROR_MESSAGE_KEY"] = "message"
    
    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    
    # JWT error handlers
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "The token has expired",
            "error": "token_expired"
        }), 401
    
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return jsonify({
            "message": "Signature verification failed",
            "error": "invalid_token"
        }), 401
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return jsonify({
            "message": "Request does not contain a valid token",
            "error": "authorization_required"
        }), 401
    
    @jwt.token_in_blocklist_loader
    def token_in_blocklist_callback(jwt_header, jwt_payload):
        return False
    
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return jsonify({
            "message": "The token has been revoked",
            "error": "token_revoked"
        }), 401
    
    # Initialize database tables
    with app.app_context():
        db.create_all()
    
    # Register blueprints
    from app.routes import tasks_bp, auth_bp, health_bp
    app.register_blueprint(tasks_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(health_bp)
    
    return app