
# Task Management

A Flask web application for managing tasks with modular user and admin interfaces.

## Project Structure

```
src/
└── tasks/
    ├── templates/           # Shared templates
    │   ├── base.html
    ├── static/              # Static assets
    │   ├── css/
    │   ├── js/
    ├── services/            # Logic
    │   ├── __init__.py
    │   ├── tasks_managment.py
    ├── models/              # Data models
    │   ├── __init__.py
    │   ├── Task.py
    ├── database/            # Database interactions
    │   ├── __init__.py
    │   ├── tasks_db.py
    ├── api/
    │   ├── TaskApp/         # User interface
    │   │   ├── templates/
    │   │   │   ├── tasks.html
    │   │   │   └── add_task.html
    │   │   ├── __init__.py
    │   │   └── routes.py
    │   └── admin/           # Admin interface
    │       ├── templates/
    │       ├── __init__.py
    │       └── routes.py
    ├── requirements.txt
    ├── setup.py
    └── run.py

```

## Setup

1. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run:
```bash
python run.py
```

## Features

- Task management interface
- Admin interface
- User task viewing and creation

## Access

- Tasks: http://localhost:8080
- Admin: http://localhost:10800
```