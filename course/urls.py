from django.urls import path
from . import views

urlpatterns = [
    path('department', views.department, name="department"),
    path('add-department', views.add_department, name="add_department"),
    path('edit-department/<int:id>', views.edit_department, name="edit_department"),
    path('remove-department/<int:id>', views.remove_department, name="remove_department"),

]