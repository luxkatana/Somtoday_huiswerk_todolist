from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# Create your views here. 
def index(_: HttpRequest) -> HttpResponse:
    return redirect("/login")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")