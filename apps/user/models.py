from rest_framework import serializers
from django.contrib.auth.models import User

# Create your models here.
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username"]
