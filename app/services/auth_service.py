from flask_jwt_extended import create_access_token
from app.services.user_service import UserService

class AuthService:
    def __init__(self):
        self.user_service = UserService()
    
    def register(self, username, email, password):
        if not username or not email or not password:
            return None, "Missing required fields"
            
        user, error = self.user_service.create_user(username, email, password)
        
        if error:
            return None, error
            
        return user, None
    
    def login(self, username, password):
        if not username or not password:
            return None, "Missing username or password"
            
        user = self.user_service.authenticate(username, password)
        
        if not user:
            return None, "Invalid username or password"
            
        access_token = create_access_token(identity=str(user.id))
        return {"user_id": user.id, "access_token": access_token}, None
    
    def get_user_profile(self, user_id: int):          
        user = self.user_service.get_user_by_id(user_id)
        
        if not user:
            return None, "User not found"
            
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }, None 