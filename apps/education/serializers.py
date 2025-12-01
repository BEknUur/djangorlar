from typing import Any,Optional
from rest_framework.serializers import (
    Serializer,
    EmailField,
    CharField,
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
    IntegerField,
    BooleanField,
    ValidationError,
)
from apps.users.models import (
    CustomUser1
)
from apps.education.models import Course, Lesson 


class CouseSeralizer(ModelSerializer):
    """
    seralizer for course model 
    """
    id=CharField(read_only=True)
    title=CharField(reqired=True,max_length=255)
    description=CharField(required=True)
    lesson_count=SerializerMethodField()

    class Meta:
        model =Course
        fields=(
            "id",
            "title",
            "description",
            "owner",
            "lesson_count",
        )
        def get_lessong_count(self,obj:Course)->int:
            return obj.lessons.filter(deleted_at__isnull=True).count()
        


class LessonSeralizer(ModelSerializer):
    """
    serializer for lesson model
    """
    id=CharField(read_only=True)
    course=PrimaryKeyRelatedField(queryset=Course.objects.all(),required=True)
    title=CharField(required=True,max_length=255)
    content=CharField(required=True)
    order=IntegerField(required=True)
    indention=IntegerField(required=True)
    is_published=BooleanField(required=False)

    class Meta:
        model=Lesson
        fields=(
            "id",
            "course",
            "title",
            "content",
            "order",
            "indention",
            "is_published",
        )
