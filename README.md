# Task Management System

## Description
This Task Management System is a simple web application built using the Django framework, designed to allow users within an organization to create, assign, track, and manage tasks effectively.

## Use Cases
- **User Registration and Authentication:** Users can register for an account and log in to access their tasks.
- **Task Creation:** Logged-in users can create tasks, assigning a title, description, due date, priority, and status.
- **Task Viewing:** Users can view a list of tasks assigned to them or created by them.
- **Task Updating:** Users can edit task details if they have the appropriate permissions.
- **Task Deletion:** Users can delete tasks they have created.

## Basic Setup Instructions

### Prerequisites
- Python 3.10.x
- Django 5.0.x
- Git

### Installation

### 1.Clone the repository:
   git clone https://github.com/Mathias-Paul/Software-Architect-and-Design-Phase-3-Project.git

### 2. Navigate to the project directory:

cd Software-Architect-and-Design-Phase-3-Project

### 3. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

### 4. Install the requirements:

pip install -r requirements.txt

### 5. Run migrations to create the database schema:

python manage.py makemigrations
python manage.py migrate

### 6. Create a superuser account to access the Django admin site:

python manage.py createsuperuser

### 7. Start the development server:

python manage.py runserver

### 8. Visit http://127.0.0.1:8000/admin in your web browser and log in with your superuser account to manage tasks.

## Other Useful Information
- **Admin Panel:** The application comes with an admin panel that can be used to manage users and tasks.
- **User Roles:** Currently, all users have the same level of access. Role-based access control is planned for future updates.
- **Security:** Do not forget to change the SECRET_KEY in the settings.py file and set DEBUG to False for production environments.
- **Tests:** Automated tests are yet to be implemented.
- **Deployment:** yet to be implemented.

Thank you :)
