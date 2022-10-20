from django.urls import path
from . import views

urlpatterns = [
    path('department', views.department, name="department"),
    path('add-department', views.add_department, name="add_department"),
    path('edit-department/<int:id>', views.edit_department, name="edit_department"),
    path('remove-department/<int:id>', views.remove_department, name="remove_department"),

    path('list-semester', views.list_semester, name="list_semester"),
    path('add-semester', views.add_semester, name="add_semester"),
    path('edit-semester/<int:id>', views.edit_semester, name="edit_semester"),
    path('remove-semester/<int:id>', views.remove_semester, name="remove_semester"),

    path('list-classes', views.list_classes, name="list_classes"),
    path('add-class', views.add_class, name="add_class"),
    path('edit-class/<int:id>', views.edit_class, name="edit_class"),
    path('remove-class/<int:id>', views.remove_class, name="remove_class"),





]