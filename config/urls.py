from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("aprel23.urls")),
    path('api2/', include("dars.urls")),
]
