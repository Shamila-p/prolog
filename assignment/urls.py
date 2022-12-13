from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/assignment',views.assignment,name="assignment"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/add-assignment',views.add_assignment,name="add_assignment"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/submitted-assignment',views.submitted_assignment,name="submitted_assignment"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/student/<int:student_id>/submitted-assignment/<int:assignment_id>/assign-mark',views.assign_mark,name="assign_mark"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/student/<int:student_id>/submitted-assignment/<int:assignment_id>/edit-mark/<int:mark_id>',views.edit_mark,name="edit_mark"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/assignment/<int:assignment_id>/edit-assignment',views.edit_assignment,name="edit_assignment"),
    path('remove-assignment/<int:assignment_id>',views.remove_assignment,name="remove_assignment"),

    path('list-module',views.list_module,name="list_module"),
    path('add-module',views.add_module,name="add_module"),
    path('remove-module/<int:module_id>',views.remove_module,name="remove_module"),

    path('view-assignments',views.view_assignments,name="view_assignments"),
    path('view-assignments/semester/<int:semester_id>',views.view_assignment_semester,name="view_assignments"),
    path('view-assignments/view-mark/<int:assignment_id>',views.view_mark,name="view_mark"),
    path('download/', views.download_file),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/upload/<int:assignment_id>', views.upload_file,name="upload_file")

]