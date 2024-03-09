# Task Management System

The Task Management System is a Django-based web application designed to help users manage their tasks efficiently. It allows users to create, update, delete, and view tasks, providing a straightforward interface for task management. The application supports user authentication, enabling personal task lists for individual users.

## Features

- User Registration and Login: Users can sign up and log in to manage their tasks.
- Task Management: Users can create new tasks, view a list of tasks, edit existing tasks, and delete tasks as needed.
- Admin Panel: Administrators can access the Django admin panel to manage users and tasks at a deeper level.

## How to Run the Software

To run the Task Management System on your local machine, follow these steps:

1. **Clone the Repository**: Clone the project repository from GitHub to your local machine.

   ```
   git clone https://github.com/Mathias-Paul/Software-Architect-and-Design-Phase-3-Project.git
   ```

2. **Navigate to the Project Directory**: Change into the project directory.

   ```
   cd Software-Architect-and-Design-Phase-3-Project
   ```

3. **Create a Virtual Environment**: (Optional but recommended) Use `virtualenv` to create an isolated Python environment for the project. If `virtualenv` is not installed, install it using `pip`.

   ```
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
   ```

4. **Install Dependencies**: Install the project's dependencies listed in `requirements.txt`.

   ```
   pip install -r requirements.txt
   ```

5. **Run Migrations**: Set up the database by running migrations.

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create an Admin User**: Create a superuser for the Django admin panel.

   ```
   python manage.py createsuperuser
   ```

7. **Start the Development Server**: Run the Django development server.

   ```
   python manage.py runserver
   ```

8. **Access the Application**: Open a web browser and navigate to `http://127.0.0.1:8000/` to access the Task Management System. Use the admin panel at `http://127.0.0.1:8000/admin/` to manage users and tasks.

For detailed documentation and more information on the features, refer to the Django documentation and the project's codebase.
