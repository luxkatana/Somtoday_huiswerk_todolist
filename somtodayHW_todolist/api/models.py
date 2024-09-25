from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    af = models.BooleanField()

    def __str__(self):
        return f"({self.owner.username}) {self.text}"