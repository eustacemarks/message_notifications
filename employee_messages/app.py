from decouple import config
from datetime import date, datetime
from emails import *
from emails.models import Email

def run():
    birthdays = find_birthdays(get_employees())
    for birthday in birthdays:
        if (Email.objects.filter(employee_id=birthday.get("id"), email_type = "birthday", created_at__year=date.today().year).count() == 0):
            message = Email.objects.create(
                employee_id=birthday.get("id"),
                content = f'Happy Birthday {birthday.get("name")} {birthday.get("lastname")}',
                email_type = "birthday",
                created_at = datetime.now(),
            )        
            print(f'Happy Birthday {birthday.get("name")} {birthday.get("lastname")}')
        else:
            print(f'birthday already sent')

if __name__ == '__main__':
    run()
