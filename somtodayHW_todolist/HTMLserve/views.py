from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from api.models import Todo

# Create your views here. 
def index(request: HttpRequest) -> HttpResponse:
    todos = Todo.objects.filter(owner=request.user).all()
    
    return render(request, "index.html", {'todos': todos})
    # return redirect("/login")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")