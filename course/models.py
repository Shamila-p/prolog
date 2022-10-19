from django.db import models
from common.models import auditModel

# Create your models here.

class Department(auditModel):
    dname= models.CharField(max_length=30)