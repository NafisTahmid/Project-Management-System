# Project-Management-System
Simple Project Management System using Django

# Django App Setup Guide

This guide will walk you through the process of setting up this Django application locally using a virtual environment.

## Prerequisites

Before starting, ensure you have the following installed on your local machine:

- **Python 3.6+**: You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Download it from [git-scm.com](https://git-scm.com/downloads).

## Steps to Clone and Run the Django App Locally

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the dependencies for this project. Open your terminal (or command prompt) and navigate to the directory where you want to set up your project.

Run the following command to create a virtual environment named `venv`:

On Windows, you may need to use:
python -m venv venv


Here's the complete content for the README.md file in Markdown format:

markdown
Copy code
# Django App Setup Guide

This guide will walk you through the process of setting up this Django application locally using a virtual environment.

## Prerequisites

Before starting, ensure you have the following installed on your local machine:

- **Python 3.6+**: You can download it from [python.org](https://www.python.org/downloads/).
- **Git**: Download it from [git-scm.com](https://git-scm.com/downloads).

## Steps to Clone and Run the Django App Locally

### 1. Create a Virtual Environment

First, create a virtual environment to isolate the dependencies for this project. Open your terminal (or command prompt) and navigate to the directory where you want to set up your project.

Run the following command to create a virtual environment named `venv`:

```bash
virtualenv venv

On Windows, you may need to use:
python -m venv venv

2. Activate the Virtual Environment
Now, activate the virtual environment:

For Windows:
venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate
Once activated, your terminal should show (venv) at the start of the prompt, indicating that the virtual environment is active.

3. Clone the Repository
Now that the virtual environment is set up, clone the repository to your local machine inside the directory of your virtual machine:
git clone https://github.com/NafisTahmid/Project-Management-System.git

4. Navigate to the Project Directory
After cloning, move into the project directory:
cd your-repository-name

5. Install Project Dependencies
With the virtual environment active, install all the required dependencies listed in the requirements.txt file. Run:
pip install -r requirements.txt

6. Set Up the Database
If your project uses a database (like SQLite, PostgreSQL, etc.), run the following command to apply any pending database migrations:
python manage.py migrate

7. Create a Superuser (Optional)
If you need admin access to your app, you can create a superuser by running:
python manage.py createsuperuser

8. Run the Development Server
Now, you're ready to run the Django development server. Start it by running:
python manage.py runserver

By default, the app will be available at:
http://127.0.0.1:8000/

9. Access the Admin Panel (Optional)
If you created a superuser, you can access the Django admin panel by visiting:
http://127.0.0.1:8000/admin/
