from django.db import models
from common.models import auditModel

# Create your models here.

class Department(auditModel):
    dname= models.CharField(max_length=30)

class Semester(auditModel):
    semname=models.CharField(max_length=30)

class Class(auditModel):
    classname=models.CharField(max_length=30)
    Semester=models.ForeignKey(Semester,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,null=True,on_delete=models.CASCADE)