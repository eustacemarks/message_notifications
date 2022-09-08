from django.urls import path
from emails import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.EmailsList.as_view(), name='email-list'),
]
