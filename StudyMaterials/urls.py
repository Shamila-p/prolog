from django.urls import path
from . import views

urlpatterns = [
    path('study-materials',views.study_materials,name="study_materials"),
    path('module/<str:module_name>',views.module,name="module"),
    path('add-materials/<str:module_name>',views.add_materials,name="add_note"),
    path('edit-materials/<int:material_id>',views.edit_materials,name="edit_materials"),
    path('remove-materials/<int:material_id>',views.remove_materials,name="remove_materials"),

]