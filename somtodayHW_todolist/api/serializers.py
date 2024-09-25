from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Todo
        fields = ['text', 'pk', 'af', 'owner', 'url']
        read_only_fields = ['pk']

