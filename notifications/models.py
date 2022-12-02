from django.db import models
from course.models import Class, Department, Semester
from member.models import Student, auditModel

# Create your models here.
class Complaint(auditModel):
    message=models.CharField(max_length=500)
    send_to= models.CharField(max_length=10)
    student=models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    department=models.ForeignKey(Department, null=True, on_delete=models.CASCADE)
    batch=models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)

class Notification(auditModel):
    message=models.CharField(max_length=500)
    send_to= models.CharField(max_length=10)