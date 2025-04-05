from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import TaskService

tasks_bp = Blueprint('tasks', __name__, url_prefix='/tasks')
task_service = TaskService()

@tasks_bp.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    current_user_id = get_jwt_identity()
    tasks = task_service.get_tasks_by_user_id(current_user_id)
    
    return jsonify({
        "tasks": [task.to_dict() for task in tasks]
    })

@tasks_bp.route('/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    current_user_id = get_jwt_identity()
    task = task_service.get_task_by_id_and_user_id(task_id, current_user_id)
    
    if not task:
        return jsonify({"message": "Task not found"}), 404
        
    return jsonify(task.to_dict())

@tasks_bp.route('/', methods=['POST'])
@jwt_required()
def create_task():
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "Invalid request data"}), 400
    
    task, error = task_service.create_task(
        data.get('title'),
        data.get('description', ''),
        data.get('status'),
        current_user_id
    )
    
    if error:
        return jsonify({"message": error}), 400
    
    if not task:
        return jsonify({"message": "Failed to create task"}), 500
        
    return jsonify({
        "message": "Task created successfully",
        "task": task.to_dict()
    }), 201

@tasks_bp.route('/<int:task_id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_task(task_id):
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "No update data provided"}), 400
    
    task, error = task_service.update_task(task_id, current_user_id, data)
    
    if error:
        return jsonify({"message": error}), 404
    
    if not task:
        return jsonify({"message": "Failed to update task"}), 500
        
    return jsonify({
        "message": "Task updated successfully",
        "task": task.to_dict()
    })

@tasks_bp.route('/<int:task_id>', methods=['DELETE'])
@jwt_required()
def delete_task(task_id):
    current_user_id = get_jwt_identity()
    success, error = task_service.delete_task(task_id, current_user_id)
    
    if error:
        return jsonify({"message": error}), 404
    
    return jsonify({"message": "Task deleted successfully"})