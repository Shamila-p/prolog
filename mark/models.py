from django.db import models

from common.models import auditModel
from member.models import Student,User
from course.models import Class, Semester, Subject

# Create your models here.
class Mark(auditModel):
    FIRST_INTERNAL="FIE"
    SECOND_INTERNAL="SIE"
    CLASS_TESTS="CTS"


    EXAM_CHOICES=[
        (FIRST_INTERNAL, "FIRST INTERNAL"),
        (SECOND_INTERNAL, "SECOND INTERNAL"),
        (CLASS_TESTS, "CLASS TESTS"),
    ]

    exam_type=models.CharField(
        max_length=3, choices=EXAM_CHOICES, null=False,default=None)
    total_score=models.CharField(max_length=50)
    marked_score=models.CharField(max_length=50)
    subject=models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    student=models.ForeignKey(Student, null=True, on_delete=models.CASCADE)
    teacher=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    class_belongs=models.ForeignKey(Class, null=True, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, null=True, on_delete=models.CASCADE)

    @property
    def exam_value(self):
        current_exam = self.exam_type
        for exam_type in Mark.EXAM_CHOICES:
            if exam_type[0] == current_exam:
                value = exam_type[1]
        return value
