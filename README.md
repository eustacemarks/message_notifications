# Message Notifications
Simple birthday message notification project 

## How install (locally)
The instructions below assumes you're already familiar with Python/Django

1. Download and clone this project's repository
2. Create a new virtual environment and activate it
3. Navigate to the project directory inside your terminal
4. run ``pip install -r requirements.txt`` to install all the project's dependencies
5. Ensure you have a local instance of the database by running:
        ``python manage.py makemigrations`` and
        ``python manage.py migrate``
6. run ``python app.py`` to queue birthday messages
7. run ``python manage.py runserver`` to run the project & open in the browser
8. go to ``http://localhost:8000/emails/`` to view messages 