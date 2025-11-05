from django.urls import include
from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import TaskViewSet

router = DefaultRouter()

router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]