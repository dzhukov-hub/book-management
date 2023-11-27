from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookApiViewSet

router = DefaultRouter()
router.register(r'book', BookApiViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
