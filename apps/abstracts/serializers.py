from rest_framework.serializers import ModelSerialiszer 

from apps.users.models import CustomUser1

class CustomUserForeignSerializer(ModelSerialiszer):
    """
    serializer for customuser model
    """
    class Meta:
        model=CustomUser1
        fields =[
            "id",
            "username",
            "email",
        ]