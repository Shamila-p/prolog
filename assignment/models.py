from django.db import models
from common.models import auditModel
from course.models import Subject
from asyncio.windows_events import NULL


# Create your models here.
class Assignment(auditModel):
    FIRST_ASSIGNMENT="F"
    SECOND_ASSIGNMENT="S"

    ASSIGNMENT_CHOICES=[
        (FIRST_ASSIGNMENT, "FIRST ASSIGNMENT"),
        (SECOND_ASSIGNMENT, "SECOND ASSIGNMENT"),
    ]

    topic=models.CharField(max_length=500)
    created_date=models.DateTimeField(auto_now=True)
    submission_date=models.DateField()
    module=models.CharField(max_length=15)
    subject=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    type=models.CharField(
        max_length=2, choices=ASSIGNMENT_CHOICES, null=False,default=NULL)
    questions=models.FileField(upload_to='files/', null=True)


    @property
    def type_value(self):
        current_type = self.type
        for type in Assignment.ASSIGNMENT_CHOICES:
            if type[0] == current_type:
                value = type[1]
        return value


class module(auditModel):
    modulename=models.CharField(max_length=10)