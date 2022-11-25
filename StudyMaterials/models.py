from django.db import models

from common.models import auditModel
from course.models import Class, Semester, Subject

# Create your models here.
class Notes(auditModel):
    NOTE="NO"
    VIDEO="VI"

    MATERIAL_CHOICES=[
        (NOTE, "Note"),
        (VIDEO, "Video"),
    ]


    filename= models.CharField(max_length=500)
    module= models.CharField(max_length=15)
    category= models.CharField(max_length=2, choices=MATERIAL_CHOICES, null=True)
    filepath= models.FileField(upload_to='files/', null=True)
    uploaded_date=models.DateTimeField(auto_now=True)
    subject=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    class_belongs=models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)

    @property
    def category_value(self):
        current_category = self.category
        for category in Notes.MATERIAL_CHOICES:
            if category[0] == current_category:
                value = category[1]
        return value


