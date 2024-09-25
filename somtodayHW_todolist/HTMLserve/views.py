from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

class TestTodo:
    def __init__(self, todo_id: int, text: str, current_state: bool=False):
        self.id = todo_id
        self.text = text
        self.af = current_state

# Create your views here. 
def index(request: HttpRequest) -> HttpResponse:
    todos = [
        TestTodo(1, "Test 1", False),
        TestTodo(2, "Test 2", False),
        TestTodo(3, "Test 3", True),
    ]
    return render(request, "index.html", {'todos': todos})
    # return redirect("/login")


def login(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")