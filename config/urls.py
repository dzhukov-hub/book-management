from django.urls import path, include
from django.contrib import admin

# from ../src.books import src.books.views
from src.books import views


urlpatterns = [
    path('api/', include('src.books.urls')),
    path('api/register/', views.user_register_send_email, name='user-register'),
    path("admin/", admin.site.urls),
]
