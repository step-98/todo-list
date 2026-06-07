# Todo List
 
A simple task management web application built with Django.
 
## Features
 
- Create, update, and delete tasks
- Mark tasks as complete or undo completion with one click
- Set optional deadlines for tasks
- Organize tasks with tags
- Tasks sorted by status (not done first) and creation date (newest first)
- Pagination on the task list
- Manage tags: create, update, delete
## Tech Stack
 
- **Python** 3.14
- **Django** 6.0.6
- **Bootstrap** 4
- **django-crispy-forms** 2.6 + crispy-bootstrap4
- **SQLite** (default Django database)
## Installation
 
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/todo-list.git
   cd todo-list
   ```
 
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```
 
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
 
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
 
5. (Optional) Load sample data:
   ```bash
   python manage.py loaddata data.json
   ```
 
6. Run the development server:
   ```bash
   python manage.py runserver
   ```
 
7. Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
