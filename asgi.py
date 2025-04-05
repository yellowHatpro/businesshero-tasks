"""
ASGI entry point for the Flask application.
This enables the app to be run with ASGI servers like Uvicorn.
"""
from app import create_app

# Import ASGI middleware to properly wrap Flask for ASGI
from asgiref.wsgi import WsgiToAsgi

# Create the Flask application
flask_app = create_app()

# Wrap the Flask application with WsgiToAsgi for ASGI compatibility
app = WsgiToAsgi(flask_app)

if __name__ == "__main__":
    import uvicorn
    import os
    
    port = int(os.getenv("PORT", 5000))
    workers = int(os.getenv("WORKERS", 4))
    
    uvicorn.run("asgi:app", host="0.0.0.0", port=port, workers=workers) 