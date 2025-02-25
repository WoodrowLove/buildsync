BuildSync - Construction Project Management System

BuildSync is a construction project management system designed to help teams efficiently manage projects, tasks, and contractors. It provides features such as user authentication, file uploads, and role-based access control.

Features
	•	User authentication (Login, Logout, Register)
	•	Project management (Create, Read, Update, Delete) with PDF plan uploads
	•	Task management with contractor assignments
	•	Contractor management with contact details and trade categories
	•	File uploads for project plans
	•	Role-based access control (Managers vs. Contractors - Future Feature)

Technology Stack
	•	Backend: Django (Python)
	•	Frontend: Django Templates + Bootstrap
	•	Database: SQLite (default), PostgreSQL (for production)
	•	Authentication: Django’s built-in authentication system
	•	File Handling: Django FileField for PDF uploads

Installation and Setup

Clone the Repository

git clone https://github.com/YOUR_GITHUB_USERNAME/buildsync.git
cd buildsync

Create and Activate Virtual Environment

python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows

Install Dependencies

pip install -r requirements.txt

Set Up Database

python manage.py makemigrations
python manage.py migrate

Create a Superuser for Admin Panel

python manage.py createsuperuser

Follow the prompts to create an admin user.

Run the Server

python manage.py runserver

Visit http://127.0.0.1:8000/ in the browser.

Usage

User Authentication
	•	Register: http://127.0.0.1:8000/users/register/
	•	Login: http://127.0.0.1:8000/users/login/
	•	Logout: Available in the navigation bar when logged in

Project Management
	•	List Projects: http://127.0.0.1:8000/projects/
	•	Create Project: http://127.0.0.1:8000/projects/create/
	•	Edit Project: http://127.0.0.1:8000/projects/<project_id>/edit/
	•	Delete Project: http://127.0.0.1:8000/projects/<project_id>/delete/
	•	Attach Plan Drawings: Upload PDFs when creating or editing projects
	•	View Plans: Click “View Plans” in the project list

Task Management
	•	List Tasks: http://127.0.0.1:8000/tasks/
	•	Create Task: http://127.0.0.1:8000/tasks/create/
	•	Edit Task: http://127.0.0.1:8000/tasks/<task_id>/edit/
	•	Delete Task: http://127.0.0.1:8000/tasks/<task_id>/delete/
	•	Assign Contractors: Select a contractor when creating or editing a task

Contractor Management
	•	List Contractors: http://127.0.0.1:8000/contractors/
	•	Create Contractor: http://127.0.0.1:8000/contractors/create/
	•	Edit Contractor: http://127.0.0.1:8000/contractors/<contractor_id>/edit/
	•	Delete Contractor: http://127.0.0.1:8000/contractors/<contractor_id>/delete/

File Uploads

Handling PDFs
	•	PDFs uploaded to Projects are stored in media/project_plans/.
	•	They are accessible via /media/ when running locally.

Enabling File Uploads in Development

Ensure settings.py includes:

import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

Modify urls.py to serve media files:

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

Deployment

Set Up a Production Database (PostgreSQL Recommended)

Modify settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': '5432',
    }
}

Run migrations:

python manage.py migrate

Collect Static Files

python manage.py collectstatic

Deploy to Render, Heroku, or DigitalOcean
	•	Heroku: Use gunicorn as WSGI server
	•	Render: Automatically detects Django projects

Future Enhancements
	•	Restrict project visibility so users only see their own projects
	•	Role-based access control for Managers vs. Contractors
	•	Task progress tracking with status updates
	•	Email notifications for upcoming task deadlines
	•	Mobile-friendly UI with improved responsiveness

Contributors

BuildSync is developed by:
	•	Aaron Wright
	•	WoodrowLove
	•	Contact: aaronw@sunnyjaymes.com
    Chad G. Peety (ChatGPT)

License

This project is licensed under the MIT License.