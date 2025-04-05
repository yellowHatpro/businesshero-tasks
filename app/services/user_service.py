from app.repositories import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()
    
    def create_user(self, username, email, password):
        # Check if user info already exists
        if UserRepository.get_by_username(username):
            return None, "Username already exists"
            
        if UserRepository.get_by_email(email):
            return None, "Email already exists"
        
        user = UserRepository.create(username, email, password)
        return user, None
    
    def get_user_by_id(self, user_id):
        return UserRepository.get_by_id(user_id)
    
    def get_user_by_username(self, username):
        return UserRepository.get_by_username(username)
    
    def authenticate(self, username, password):
        user = UserRepository.get_by_username(username)
        
        if not user or not user.check_password(password):
            return None
        
        return user 