from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import auditModel
from course.models import Class, Department


class User(AbstractUser, auditModel):
    STUDENT = "ST"
    TEACHER = "TR"
    PRINCIPAL = "PR"

    ROLES_CHOICES = [
        (STUDENT, "Student"),
        (TEACHER, "Teacher"),
        (PRINCIPAL, "Principal"),
    ]

    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=60)
    profile_image = models.ImageField(upload_to='profile_image',default='default-avatar.jpg',null=True)
    role = models.CharField(
        max_length=2, choices=ROLES_CHOICES, null=False)
    department = models.ForeignKey(Department, null=True, on_delete=models.CASCADE)

    @property
    def profile_image_url(self):
        try:
            url = self.profile_image.url
        except ValueError:
            url = ""
        return url


class Teacher(auditModel):
    HOD = "HD"
    ASSISTANT_PROFESSOR = "AST"
    ASSOCIATE_PROFESSOR = "ASO"

    POSITION_CHOICES = [
        (HOD, "Hod"),
        (ASSISTANT_PROFESSOR, "Assistant professor"),
        (ASSOCIATE_PROFESSOR, "Associate professor"),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    position = models.CharField(
        max_length=3, choices=POSITION_CHOICES, null=False)
        

    @property
    def position_value(self):
        current_position = self.position
        for position in Teacher.POSITION_CHOICES:
            if position[0] == current_position:
                value = position[1]
        return value


class Student(auditModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    batch = models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    admsn_no=models.CharField(max_length=6,null=True)
    parent_name = models.CharField(max_length=30)
    parent_mobile = models.CharField(max_length=15)
