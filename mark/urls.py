from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/mark',views.mark,name="mark"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/view-marks',views.view_marks,name="view_marks"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/mark/student/<int:student_id>/add-mark',views.add_mark,name="add_mark"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/mark/student/<int:student_id>/edit-mark',views.edit_mark,name="edit_mark"),

    path('performance',views.performance,name="performance"),
    path('performance-display/<str:exam_type>',views.performance_display,name="performance_display"),

]