from . import views
from django.urls import path, register_converter
from attendence.converters import DateConverter


register_converter(DateConverter, 'date')

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/attendence',views.attendence,name="attendence"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/add-attendence',views.add_attendence,name="add_attendence"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/edit-attendence',views.edit_attendence,name="edit_attendence"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/view-attendence',views.view_attendence,name="edit_attendence"),

    # path('attendence',views.student_attendence,name="student_attendence"),
    # path('attendence/subject/<int:subject_id>',views.view_student_attendence,name="view_student_attendence"),
    # path('attendence/subject/<int:subject_id>/view-attendence',views.view,name="view"),
]