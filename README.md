# Task Manager

Task Manager is an application build in Django, Django REST Framework and PostgreSQL that allows to create, read, update and delete tasks. Moreover, tracking of history changes in database is implementated which allows user to find status of specific task in the past. Tasks list and historical actions list have filter feature to make it easier to search for more precisily. 


## Technologies

- Python 3.11.4
- PostgreSQL 16.1
- Django 5.0.1
- django-dbbackup 4.1.0
- django-filter 23.5
- django-simple-history 3.4.0
- djangorestframework 3.14.0
- psycopg2 2.9.9

## Setup


1. Install required Python packages using `pip install -r requirements.txt` command in Terminal
   
2. Create task-manager-db PostgreSQL database - deafult connection settings in settings.py file are:

        'NAME': 'task-manager-db'
        'USER': 'postgres'
        'PASSWORD': 'postgres'
        'HOST': 'localhost'
        'PORT': '5432'

If your database configuration is different from above one you should change it in settings.py file (line 86).

Now, you need to run some command in Terminal in task-manager directory:

3. Create superuser by running `python manage.py createsuperuser` command

4. Run command `python manage.py makemigrations`

5. Run command `python manage.py migrate`

6. Run command `python manage.py runserver`


## API Endpoints:

- http://127.0.0.1:8000/task_list/ - read tasks list data
- http://127.0.0.1:8000/history/ - read historical actions data
- http://127.0.0.1:8000/create/ - create task
- http://127.0.0.1:8000/update/ID/ - update task with given ID
- http://127.0.0.1:8000/delete/ID/ - delete task with given ID
- http://127.0.0.1:8000task_detail/ID/ - read task data with given ID


   
