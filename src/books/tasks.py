from celery import shared_task
from django.core.mail import send_mail
from .models import CustomUser


@shared_task
def send_welcome_email(user_id):
    print("send welcome email started")
    user = CustomUser.objects.get(id=user_id)
    subject = 'Welcome to Boook Manage App!'
    message = f'Dear Guest {user.username},\n\nThank you for registering in our Book Management System!'
    send_mail(subject, message, 'noreply@bookmanage.com', [user.email])
    print(f"Sending email user: {user_id} to {user.email}")
