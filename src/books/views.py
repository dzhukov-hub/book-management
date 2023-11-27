from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from . import models, serializers
from rest_framework import viewsets
from .tasks import send_welcome_email

# Create your views here.


class BookApiViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


@api_view(['POST'])
def user_register_send_email(request):
    serializer = serializers.UserSerializer(data=request.data)
    if serializer.is_valid():
        # Check for the existence of a user with this username
        username = serializer.validated_data.get('username')
        if models.CustomUser.objects.filter(username=username).exists():
            return Response({"error": "A user with this username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        # send welcome email
        # send_welcome_email.delay(user.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
