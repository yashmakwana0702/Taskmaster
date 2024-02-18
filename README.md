# Taskmaster
# Taskmaster



This is a simple Django web application for managing tasks. Users can register, log in, create, view, update, and delete tasks.

## Installation

1. Clone the repository:

```bash
git clone 
cd Taskmaster
pip install -r requirements.txt
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
```

#### The application should now be accessible at http://localhost:8000/.

## Test
```python manage.py test```


## Authentication
- you can create superuser for Django Admin
- you can signup and login 

## Endpoints

### List all tasks
- GET `/tasks/`

### Retrieve a single task by ID
- GET `/tasks/<task_id>/`

### Create a new task
- POST `/tasks/`

### Update an existing task
- PUT `/tasks/<task_id>/`

### Delete a task
- DELETE `/tasks/<task_id>/`

## Permissions
- Users can only update or delete tasks that they own.

## Error Handling
- Errors are returned with appropriate status codes and error messages.
