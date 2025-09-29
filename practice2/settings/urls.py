#DJANGO modules
from django.contrib import admin
from django.urls import path


# project modules 

urlpatterns = [
    path('admin/', admin.site.urls),
    
]
