from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    return redirect("/login")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")
