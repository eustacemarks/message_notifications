from django.shortcuts import render
from django.views import generic
from emails.models import *
import requests
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class EmailsList(generic.ListView):
    model = Email
    context_object_name = 'email_list'
