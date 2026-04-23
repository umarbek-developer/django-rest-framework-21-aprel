from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet
from django.urls import path, include


r = DefaultRouter()

r.register("category", CategoryViewSet)
r.register("product", ProductViewSet)


urlpatterns = [
    path("", include(r.urls))
]

