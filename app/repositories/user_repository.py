from app import db
from app.models.user import User

class UserRepository:
    @staticmethod
    def create(username, email, password):
        try:
            user = User()
            user.username = username
            user.email = email
            user.set_password(password)
            
            db.session.add(user)
            db.session.commit()
            
            return user
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_by_id(user_id):
        try:
            return User.query.get(user_id)
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_by_username(username):
        try:
            return User.query.filter_by(username=username).first()
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_by_email(email):
        try:
            return User.query.filter_by(email=email).first()
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update(user):
        try:
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def delete(user):
        try:
            db.session.delete(user)
            db.session.commit()
            return True 
        except Exception as e:
            db.session.rollback()
            raise e
