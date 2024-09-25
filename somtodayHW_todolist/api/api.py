from rest_framework import routers, viewsets
from .serializers import TodoSerializer
from .models import Todo


r = routers.DefaultRouter()


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user).all()

r.register('todo', TodoViewSet, 'todo')