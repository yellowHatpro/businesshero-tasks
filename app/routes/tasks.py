from flask import Blueprint, jsonify

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def index():
    return jsonify({"message": "Task Management"})