

# Project Hosting Documentation

This documentation provides a step-by-step guide for setting up and hosting the Django project locally, along with instructions on pushing it to GitHub.

---

## Prerequisites

Before starting, make sure you have the following installed:

- Python (>=3.6)
- pip (Python package installer)
- Git
- Virtual Environment

---

## Step 1: Create a Virtual Environment

1. Create a Virtual Environment for the project:

    ```bash
    python -m venv venv
    ```

2. Navigate to virtual env directory and activate the Virtual Environment:

    - For **Windows**:

      ```bash
      cd venv
      source Scripts/activate
      ```

    - For **macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

    You should see `(venv)` at the beginning of your command line, indicating that the virtual environment is active.

---

## Step 2: Clone the Repository

1. Navigate inside inside your virtual env and clone the GitHub repository to your local machine:

    ```bash
     git clone https://github.com/NafisTahmid/Project-Management-System.git




    ```

    Replace `yourusername` and `yourrepository` with your actual GitHub username and repository name.

2. Navigate to the project directory:

    ```bash
    cd your repository
    ```
---

## Step 3: Install Project Dependencies

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

    If `requirements.txt` is not already present, you can generate it by running:

    ```bash
    pip freeze > requirements.txt
    ```

---

## Step 4: Set Up Database

1. Run migrations to set up your database:

    ```bash
    python manage.py migrate
    ```

2. Create a superuser to access the Django admin panel (optional):

    ```bash
    winpty python manage.py createsuperuser
    ```

    Follow the prompts to create the admin user.

---

## Step 5: Install Additional Libraries (if required)

If you've installed additional libraries such as `crispy_forms` and `crispy-bootstrap5`, ensure they are included in `requirements.txt` and installed as part of your dependencies.

For example:

```bash
pip install crispy-forms crispy-bootstrap5
```

## Step 6: Run the development server
Once all dependencies are installed, and the database is set up, start the development server:

  ```bash
  python manage.py runserver
  ```
## Step 7: Access the Admin Panel (Optional)
If you created a superuser, you can access the Django admin panel by visiting:

```bash
http://127.0.0.1:8000/admin/
```

# API Documentation

## Getting Started with Postman

1. **Start Postman**  
   Open Postman and create a new request for each endpoint as described below.

2. **Set URL**  
   Set the URL for your API requests to `http://127.0.0.1:8000/api/`.

3. **Select HTTP Method**  
   Choose the appropriate HTTP method (GET, POST, PUT, DELETE) based on the endpoint.

4. **Request Body**  
   For POST and PUT requests, make sure to set the request body in JSON format.

5. **Headers**  
   Set the `Content-Type` header to `application/json` for all requests that send a body.

6. **Authentication**  
   If your API requires authentication, add the necessary authorization token in the **Authorization** tab of Postman (e.g., Bearer Token).

### Base URL  
The base URL for all the API endpoints is:  
`http://127.0.0.1:8000/api/`

---

## User APIs

### POST /register
- **Endpoint:** `/api/users/register/`
- **Method:** POST
- **Description:** This endpoint registers a new user.

### POST /login
- **Endpoint:** `/api/users/login/`
- **Method:** POST
- **Description:** This endpoint allows users to log in.

### POST /logout
- **Endpoint:** `/api/users/logout/`
- **Method:** POST
- **Description:** This endpoint logs the user out.
- **Request Body:** None (Logout action does not require a body)

### POST /change_password
- **Endpoint:** `api/users/change_password/`
- **Method:** POST
- **Description:** This endpoint changes user password

### GET /user-details/{pk}
- **Endpoint:** `/api/users/user-details/{pk}/`
- **Method:** GET
- **Description:** This endpoint retrieves the details of a specific user by their ID (pk).
- **Parameters:**
  - `pk`: The primary key (ID) of the user.

### PUT /update-user/{pk}
- **Endpoint:** `/api/users/{pk}/`
- **Method:** PUT
- **Description:** This endpoint allows updating the user details by their ID (pk).

### DELETE /delete-user/{pk}
- **Endpoint:** `/api/users/delete-user/{pk}/`
- **Method:** DELETE
- **Description:** This endpoint deletes a user by their ID (pk).

---

## Project APIs

### GET /home
- **Endpoint:** `/api/home/`
- **Method:** GET
- **Description:** This endpoint returns a welcome message or general information about the application.

### GET /projects
- **Endpoint:** `/api/projects/`
- **Method:** GET
- **Description:** This endpoint returns a list of all projects.

### POST /create-project
- **Endpoint:** `/api/create-project/`
- **Method:** POST
- **Description:** This endpoint allows the creation of a new project.

### GET /project-details/{pk}
- **Endpoint:** `/api/project-details/{pk}/`
- **Method:** GET
- **Description:** This endpoint retrieves the details of a specific project by its ID (pk).
- **Parameters:**
  - `pk`: The primary key (ID) of the project.

### PUT /update-project/{pk}
- **Endpoint:** `/api/update-project/{pk}/`
- **Method:** PUT
- **Description:** This endpoint allows updating a project's details by its ID (pk).

### DELETE /delete-project/{pk}
- **Endpoint:** `/api/delete-project/{pk}/`
- **Method:** DELETE
- **Description:** This endpoint deletes a project by its ID (pk).

---

## Task APIs

### POST /create-task/{pk}
- **Endpoint:** `/api/create-task/{pk}/`
- **Method:** POST
- **Description:** This endpoint allows the creation of a task for a specific project by its project ID (pk).

### GET /tasks
- **Endpoint:** `/api/tasks/`
- **Method:** GET
- **Description:** This endpoint returns a list of all tasks.

### GET /task-details/{pk}
- **Endpoint:** `/api/task-details/{pk}/`
- **Method:** GET
- **Description:** This endpoint retrieves the details of a specific task by its ID (pk).

### PUT /update-task/{project_pk}/{pk}
- **Endpoint:** `/api/update-task/{project_pk}/{pk}/`
- **Method:** PUT
- **Description:** This endpoint allows updating the details of a task within a specific project.

### DELETE /delete-task/{pk}
- **Endpoint:** `/api/delete-task/{pk}/`
- **Method:** DELETE
- **Description:** This endpoint deletes a task by its ID (pk).

---

## Comment APIs

### GET /comment-details/{task_pk}/{pk}
- **Endpoint:** `/api/comment-details/{task_pk}/{pk}/`
- **Method:** GET
- **Description:** This endpoint retrieves a specific comment on a task.

### DELETE /delete-comment/{pk}
- **Endpoint:** `/api/delete-comment/{pk}/`
- **Method:** DELETE
- **Description:** This endpoint deletes a comment by its ID (pk).

### POST /post-comment/{pk}
- **Endpoint:** `/api/post-comment/{pk}/`
- **Method:** POST
- **Description:** This endpoint allows posting a new comment to a task by its task ID (pk).
