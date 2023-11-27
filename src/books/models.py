from django.db import models
from django.utils import timezone

# Create your models here.


# Model represents books with attributes: title, author, year of publication and ISBN.
class Book(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=50)
    year_of_publication = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.year_of_publication}, ISBN: {self.isbn}"


# Model represents username, email and registration date.
class CustomUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}, Registration Date: {self.registration_date}"
