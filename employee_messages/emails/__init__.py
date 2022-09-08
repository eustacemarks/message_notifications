import requests
from pathlib import Path
from emails.birthdays import Birthday
from decouple import config

def get_employees():
    response = requests.get(config('EMPLOYEES_URI'), headers={
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    })
    return response.json()

def find_birthdays(employees):
    birthday = Birthday(employees)
    return birthday.find_birthdays()
