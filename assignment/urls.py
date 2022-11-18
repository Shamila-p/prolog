from django.urls import path
from . import views

urlpatterns = [
    path('assignment',views.assignment,name="assignment"),
    path('add-assignment',views.add_assignment,name="add_assignment"),
    path('edit-assignment/<int:assignment_id>',views.edit_assignment,name="edit_assignment"),
    path('remove-assignment/<int:assignment_id>',views.remove_assignment,name="remove_assignment"),

    path('list-module',views.list_module,name="list_module"),
    path('add-module',views.add_module,name="add_module"),
    path('remove-module/<int:module_id>',views.remove_module,name="remove_module"),

]