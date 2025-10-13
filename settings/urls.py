# Django modules
from django.contrib import admin
from django.urls import path

# Project modules

urlpatterns = [
    path('admin/', admin.site.urls),
]
