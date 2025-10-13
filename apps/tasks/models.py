# Python modules + Third party modules

# Django modules
from django.db.models import (
    CharField,
    TextField,
    IntegerField,
    ForeignKey,
    ManyToManyField,
    UniqueConstraint,
    PROTECT,
    CASCADE,
)
from django.contrib.auth.models import User

# Project modules
from apps.abstracts.models import AbstractBaseModel


class Project(AbstractBaseModel):
    """
    Represent the project in a system
    """

    NAME_MAX_LEN = 255

    name = CharField(
        max_length=NAME_MAX_LEN,
    )
    author = ForeignKey(
        to=User,
        on_delete=PROTECT,
        related_name="owned_projects",
    )
    users = ManyToManyField(
        to=User,
        blank=True,
        related_name="joined_projects",
    )

    def __repr__(self) -> str:
        """Returns the official string representation of the object."""
        return f"Project(id={self.id}, name={self.name})"

    def __str__(self) -> str:
        """Returns the string representation of the object."""
        return self.name


class Task(AbstractBaseModel):
  

    NAME_MAX_LEN = 255
    STATUS_TODO = 1
    STATUS_TODO_LABEL = "To Do"
    STATUS_IN_PROGRESS = 2
    STATUS_IN_PROGRESS_LABEL = "In Progress"
    STATUS_DONE = 3
    STATUS_DONE_LABEL = "Done"
   
    STATUS_CHOICES = {
        STATUS_TODO: STATUS_TODO_LABEL,
        STATUS_IN_PROGRESS: STATUS_IN_PROGRESS_LABEL,
        STATUS_DONE: STATUS_DONE_LABEL,
    }
    
    title=CharField(
        max_length=NAME_MAX_LEN, 
        db_index=True,
    )

    description =TextField(
        blank=True, 
        null=True,
    )
    status=IntegerField(
        choices=STATUS_CHOICES,
        default=STATUS_TODO,
    )

    project=ForeignKey(
        to=Project, 
        on_delete=CASCADE, 
      
    )
    assigness=ManyToManyField(
        to=User, 
        through='UserTask', 
        through_fields=('task','user'),
        blank=True,
    )

    parent=ForeignKey(
        to='self',
        on_delete=CASCADE, 
        blank=True, 
        null=True,
    )

   

class UserTask(AbstractBaseModel):
  
    task = ForeignKey(
        to=Task,
        on_delete=CASCADE,
    )
    user = ForeignKey(
        to=User,
        on_delete=CASCADE,
    )

    class Meta:
       

        # unique_together = ("task", "user")
        constraints = [
            UniqueConstraint(
                fields=["task", "user"],
                name="unique_task_user",
            ),
        ]
