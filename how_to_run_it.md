How to Run This Project (Step-by-Step)
Follow these steps carefully to get the "Pinspire" API up and running on your local machine:

1. Prerequisites
Python 3.x: Ensure you have Python installed.

PostgreSQL Database: You need a running PostgreSQL server.

git: For cloning the project later.

2. Project Setup
Create Project Directory: If you haven't already, create a directory for your project (e.g., pinspire_project).

Save Files: Ensure all the provided Python files (from pinspire_project/settings.py, pinspire_project/urls.py, pinspire_project/wsgi.py, manage.py, and all files in the core/ directory) are correctly placed in their respective locations within this directory structure. Also, make sure db_schema.sql is at the root.

pinspire_project/
├── pinspire_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── __init__.py
│   ├── urls.py
│   ├── views.py
│   ├── utils.py
│   └── middlewares.py
├── db_schema.sql
└── manage.py

3. Install Python Dependencies
Open your terminal or command prompt, navigate to the root of your pinspire_project directory (where manage.py is located), and run:

pip install Django psycopg2-binary PyJWT

4. Set Environment Variables
The project uses environment variables for database connection details and JWT secrets. Set these in your terminal session before running the server:

export DB_NAME="pinspire_db"
export DB_USER="pinspire_user"
export DB_PASSWORD="pinspire_password"
export DB_HOST="localhost" # Or the IP/hostname of your PostgreSQL server
export DB_PORT="5432"      # Default PostgreSQL port
export SECRET_KEY="your-very-secret-django-key-for-jwt" # Make this a strong, unique key!

Note for Windows Users: Use set instead of export (e.g., set DB_NAME=pinspire_db).

5. Setup PostgreSQL Database
Connect to PostgreSQL:
Open a PostgreSQL client (like psql in your terminal) as an administrative user:

psql -U your_postgres_admin_user

(Replace your_postgres_admin_user with an actual admin username, e.g., postgres).

Create Database and User:
Execute these SQL commands within the psql prompt:

CREATE DATABASE pinspire_db;
CREATE USER pinspire_user WITH PASSWORD 'pinspire_password';
GRANT ALL PRIVILEGES ON DATABASE pinspire_db TO pinspire_user;
\q

(The \q command exits psql).

Apply Database Schema:
Navigate back to your pinspire_project root directory in the terminal and run the db_schema.sql file:

psql -U pinspire_user -d pinspire_db -f db_schema.sql

6. Run the Django Development Server
From the root of your pinspire_project directory (where manage.py is), execute:

python manage.py runserver

You should see output indicating the server is running, usually at http://127.0.0.1:8000/.

7. Test the API
You can use tools like curl, Postman, Insomnia, or even your browser to test the endpoints. Refer to the previous instructions for example curl commands for registration, login, pin upload, and pin management.