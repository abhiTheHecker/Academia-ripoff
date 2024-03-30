# from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

# urls go here

urlpatterns = [
    path("", views.index, name='slash'),
    path("index", views.index, name='index'),
    path("login", views.login, name='login'),
    path("attendance", views.attendance, name='attendance'),
    path("marks", views.marks, name='marks'),
    path("details", views.details, name='details'),
    path("error", views.error, name='error')
]
