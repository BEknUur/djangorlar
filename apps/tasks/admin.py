# Python modules
from typing import Optional, Sequence

# Django modules
from django.contrib.admin import ModelAdmin, register
from django.core.handlers.wsgi import WSGIRequest

# Project modules
from apps.tasks.models import Task, UserTask, Project


@register(Project)
class ProjectAdmin(ModelAdmin):
    """
    Project admin configuration class.
    """

    list_per_page=25
    list_display = (
        'id',
        'name',
        'author',
        'created_at'
    )
    list_display_links = (
        'id',
        
    )
    search_fields = (
        'name',
        'id'
    )
    ordering =(
        '-updated_at',
    )
    list_filter =(
        'updated_at',
    )
    readonly_fields =(
        'created_at',
        'updated_at',
        'deleted_at',
    )
    save_on_top =True 

    fieldsets =(
        ( 
            "Project Information",
            { 
                'fields':(
                    'name',
                    'author',
                    'users',
                )
            }
        ),
        (
            "Timestamps",
            {
                'fields':(
                    'created_at',
                    'updated_at',
                    'deleted_at',
                )
            }
        )
    )


 

    def has_add_permission(self, request: WSGIRequest) -> bool:
        """Disable add permission."""
        return False

    def has_delete_permission(self, request: WSGIRequest, obj: Optional[Project] = None) -> bool:
        """Disable delete permission."""
        return False

    def has_change_permission(self, request: WSGIRequest, obj: Optional[Project] = None) -> bool:
        """Disable change permission."""
        return False

    


@register(Task)
class TaskAdmin(ModelAdmin):
    """
    Task admin configuration class.
    """

    ...


@register(UserTask)
class UserTaskAdmin(ModelAdmin):
    """
    UserTask admin configuration class.
    """

    ...
