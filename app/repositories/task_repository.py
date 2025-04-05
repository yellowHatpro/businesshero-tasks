from app import db
from app.models.task import Task

class TaskRepository:
    @staticmethod
    def create(title, description, status, user_id):
        try:
            task = Task()
            task.title = title
            task.description = description
            task.status = status
            task.user_id = user_id
            
            db.session.add(task)
            db.session.commit()
            
            return task
        except Exception as e:
            db.session.rollback()
            raise e
        
    @staticmethod
    def get_by_id(task_id):
        try:
            return Task.query.get(task_id)
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_by_user_id(user_id):
        try:
            return Task.query.filter_by(user_id=user_id).all()
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def get_by_id_and_user_id(task_id, user_id):
        try:
            return Task.query.filter_by(id=task_id, user_id=user_id).first()
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def update(task):
        try:
            db.session.commit()
            return task
        except Exception as e:
            db.session.rollback()
            raise e
    
    @staticmethod
    def delete(task):
        try:
            db.session.delete(task)
            db.session.commit()
            return True 
        except Exception as e:
            db.session.rollback()
            raise e
