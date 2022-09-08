import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "employee_messages.settings")
import django
django.setup()

import requests
from decouple import config
from datetime import datetime, timedelta
from emails.models import Email

LEAP_DAY_MONTH = datetime(2000,2,29,16,20).strftime('%d-%m')

class Birthday:

    __birthdays = []
    def __init__(self, employees=[]):
        self.employees = employees
        

    def find_birthdays(self):
        for employee in self.employees:
            if employee.get('dateOfBirth') and self.is_birthday_today(employee.get('dateOfBirth')):
                self.__birthdays.append(employee)

        return self.__birthdays
    

    def is_birthday_today(self, birthday):
        if self.not_leap_year(birthday) and (self.birth_day_month(birthday) == LEAP_DAY_MONTH):
            birthday = (datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S") + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S")
        
        birthday = self.birth_day_month(birthday) 
        return bool(birthday == datetime.now().strftime('%d-%m'))
    
    
    def birth_day_month(self, birthday):
        return (datetime.strptime(birthday, '%Y-%m-%dT%H:%M:%S').strftime('%d-%m'))
    
    
    def not_leap_year(self,birthday):
        year = datetime.strptime(birthday, "%Y-%m-%dT%H:%M:%S").year
        
        if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
            return True
        else:
            return False


