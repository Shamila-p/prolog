from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
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
    profile_image = models.ImageField(upload_to='profile_image')
    role = models.CharField(
        max_length=2, choices=ROLES_CHOICES, null=False)

    @property
    def profile_image_url(self):
        try:
            url = self.profile_image.url
        except ValueError:
            url = ""
        return url
