from rest_framework import serializers
from .models import Book, CustomUser


# Serializer for handling Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "year_of_publication", "isbn")


# Serializer for handling User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'registration_date')
