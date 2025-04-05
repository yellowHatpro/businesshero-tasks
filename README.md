# BusinessHero Tasks

A Flask backend with PostgreSQL integration.

## Setup

1. Make sure you have Python 3.13+ installed
2. Install dependencies:

   ```
   uv pip install -r requirements.txt
   ```

3. Set up environment variables:

   - Create a `.env` file in the root directory (use `.env.example` as a reference)
   - Update the PostgreSQL connection details

4. Initialize the database:

   ```
   python setup_db.py
   ```

5. Run the application:
   ```
   python main.py
   ```

## API Endpoints

- `GET /`: Welcome message
- `GET /users`: Get all users
- `POST /users`: Create a new user

## Requirements

- Python 3.13+
- PostgreSQL
- Flask and related packages (see requirements.txt)
