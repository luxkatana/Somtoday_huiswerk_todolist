from django.urls import path, include
from .api import r

urlpatterns = [
    path('', include(r.urls))
]