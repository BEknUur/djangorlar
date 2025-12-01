from django.db.models import (
    CharField,
    TextField,
    BooleanField,
    DateTimeField,
    ForeignKey,
    DecimalField,
    PositiveSmallIntegerField,
    CASCADE
)

from apps.abstracts.models import AbstractBaseModel
from apps.users.models import CustomUser1
from django.core.validators import MaxValueValidator


TITLE_MAX_LENGTH =255 

class Course(AbstractBaseModel):
    """
    Course model
    
    """

    title=CharField(max_length=TITLE_MAX_LENGTH)
    is_active=BooleanField(default=True)
    description=TextField(blank=True,null=True)
    owner=ForeignKey(CustomUser1,on_delete=CASCADE,related_name="ownded_courses")



class Lesson(AbstractBaseModel):
    """
    Lesson model
    """

    ORDER_MAX_DIGITS:int=5
    ORDER_DECIMAL_PLACES:int=2 
    INDENTION_MAX_VALUE:int=5

    course=ForeignKey(Course,on_delete=CASCADE,related_name="lessons")
    title=CharField(max_length=TITLE_MAX_LENGTH)
    content=TextField()
    order=DecimalField(
        max_digits=ORDER_MAX_DIGITS,decimal_places=ORDER_DECIMAL_PLACES)
    indention=PositiveSmallIntegerField(validatord=[MaxValueValidator(INDENTION_MAX_VALUE)])
    is_published=BooleanField(default=False)
    