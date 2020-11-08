from django.http import HttpRequest
from rest_framework.decorators import api_view
from django.contrib import auth
from rest_framework.response import Response
from django.contrib.auth.models import User
from ..utils.serializer import UserSerializer
from django.db import IntegrityError
from django.core.exceptions import ValidationError

@api_view(['POST'])
def updateUser(request: HttpRequest):
    user : User = request.user
    new_email = request.POST['email']

    user.email = new_email
    serializer = UserSerializer(user)

    try:
        user.full_clean()
        user.save()
    except (ValidationError, IntegrityError):
        return Response(status = 500, data = {"error_message": "Une erreur a survenue lors de la modification."})

    return Response(serializer.data)
