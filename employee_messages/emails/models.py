from django.db import models
from datetime import datetime

class Email(models.Model):
    employee_id = models.IntegerField()
    content = models.TextField()
    email_type = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now)
    is_sent = models.BooleanField(default=False)

