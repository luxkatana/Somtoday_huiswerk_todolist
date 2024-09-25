from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from api.models import Todo

# Create your views here. 
def index(request: HttpRequest) -> HttpResponse:
    if request.user.id is not None:
        todos = Todo.objects.filter(owner=request.user).all()
        return render(request, "index.html", {'todos': todos})
    
    return redirect("/login")
    # return redirect("/login")


def login(request: HttpRequest) -> HttpResponse:
    if request.user.id is not None:
        return redirect("/")
    return render(request, "login.html")