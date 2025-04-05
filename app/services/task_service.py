from app.repositories import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()
    
    def get_tasks_by_user_id(self, user_id):
        return TaskRepository.get_by_user_id(user_id)
    
    def get_task_by_id_and_user_id(self, task_id, user_id):
        return TaskRepository.get_by_id_and_user_id(task_id, user_id)
    
    def create_task(self, title, description, status, user_id):
        if not title:
            return None, "Title is required"
        
        # Validate status
        valid_statuses = ['pending', 'in-progress', 'completed']
        if status and status not in valid_statuses:
            return None, f"Status must be one of: {', '.join(valid_statuses)}"
            
        # Default to pending if no status provided
        status = status if status else 'pending'
            
        task = TaskRepository.create(title, description, status, user_id)
        return task, None
    
    def update_task(self, task_id, user_id, data):
        task = TaskRepository.get_by_id_and_user_id(task_id, user_id)
        
        if not task:
            return None, "Task not found"
        
        # Validate status if present
        if 'status' in data:
            valid_statuses = ['pending', 'in-progress', 'completed']
            if data['status'] not in valid_statuses:
                return None, f"Status must be one of: {', '.join(valid_statuses)}"
            task.status = data['status']
            
            # Update completed field for compatibility
            task.completed = (data['status'] == 'completed')
            
        if 'title' in data:
            task.title = data['title']
            
        if 'description' in data:
            task.description = data['description']
        
        # For backward compatibility
        if 'completed' in data:
            task.completed = data['completed']
            # Update status to match completed value
            task.status = 'completed' if data['completed'] else 'pending'
            
        TaskRepository.update(task)
        return task, None
    
    def delete_task(self, task_id, user_id):
        task = TaskRepository.get_by_id_and_user_id(task_id, user_id)
        
        if not task:
            return False, "Task not found"
            
        TaskRepository.delete(task)
        return True, None 