from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/assignment',views.assignment,name="assignment"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/add-assignment',views.add_assignment,name="add_assignment"),
    path('class/<int:class_id>/semester/<int:semester_id>/subject/<int:subject_id>/assignment/<int:assignment_id>/edit-assignment',views.edit_assignment,name="edit_assignment"),
    path('remove-assignment/<int:assignment_id>',views.remove_assignment,name="remove_assignment"),

    path('list-module',views.list_module,name="list_module"),
    path('add-module',views.add_module,name="add_module"),
    path('remove-module/<int:module_id>',views.remove_module,name="remove_module"),

    path('view-assignments',views.view_assignments,name="view_assignments"),
    path('download/', views.download_file)

]