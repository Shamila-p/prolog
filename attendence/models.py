from django.db import models
from common.models import auditModel
from member.models import Student,User
from course.models import Subject,Class
# Create your models here.

class Attendence(auditModel):
    date=models.DateField()
    subject=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    teacher=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    is_present=models.BooleanField(default=False)