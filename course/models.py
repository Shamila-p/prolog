from django.db import models
from common.models import auditModel



# Create your models here.

class Department(auditModel):
    dname = models.CharField(max_length=30)
    hod = models.ForeignKey("member.User", null=True, on_delete=models.CASCADE,related_name="hod_name")


class Semester(auditModel):
    semname = models.CharField(max_length=30)


class Class(auditModel):
    classname = models.CharField(max_length=30)
    Semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    tutor = models.ForeignKey("member.User", null=True, on_delete=models.CASCADE)


class Subject(auditModel):
    subjectname=models.CharField(max_length=50)
    subjectcode=models.CharField(max_length=50,null=True)
    assigned_to=models.ForeignKey("member.User", null=True, on_delete=models.CASCADE,related_name="assigned")
    tutor = models.ForeignKey("member.User", null=True, on_delete=models.CASCADE)
    class_belongs = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)



class EditSubject(auditModel):
    subjectname=models.CharField(max_length=50)
    subjectcode=models.CharField(max_length=50,null=True)
    assigned_to=models.ForeignKey("member.User", null=True, on_delete=models.CASCADE,related_name="assigned_request")
    tutor = models.ForeignKey("member.User", null=True, on_delete=models.CASCADE)
    class_belongs = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)




