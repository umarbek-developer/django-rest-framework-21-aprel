from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import NotebookViewSet


r = DefaultRouter()

r.register("notebook", NotebookViewSet)


urlpatterns = [
    path('', include(r.urls))
]


