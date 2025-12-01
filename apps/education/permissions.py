from typing import Any
from rest_framework.permissions import BasePermission
from rest_framework.request import Request 
from rest_framework.viewsets import ViewSet

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request:Request,view:ViewSet,obj:Any)->bool:
        """
        Return True if permission is granted, False otherwise.
        """
        return obj.owner==request.user
    

class IsCourseOwner(BasePermission):
    def has_object_permisson(
            self,
            request:Request,
            view:ViewSet,
            obj:Any
    )->bool:
        """
        Return if the user and the course ownerr true the boolean type 
        """

        return obj.owner==request.user