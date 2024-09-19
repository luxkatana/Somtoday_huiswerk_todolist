from django.urls import path
from . import views # noqa

urlpatterns = [
    path("index/", views.index),
    path("login/", views.login)
    
]