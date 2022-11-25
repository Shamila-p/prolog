from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/attendence',views.attendence,name="attendence"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/add-attendence',views.add_attendence,name="add_attendence"),
    # path('class/<int:class_id>/subject/<int:subject_id>/student/<int:student_id>/edit-attendence',views.edit_attendence,name="edit_attendence"),
]