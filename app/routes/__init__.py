# routes package

from .tasks import tasks_bp
from .auth import auth_bp

__all__ = ['tasks_bp', 'auth_bp']