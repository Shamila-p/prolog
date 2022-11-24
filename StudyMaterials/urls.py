from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/subject/<int:subject_id>/study-materials',views.study_materials,name="study_materials"),
    path('class/<int:class_id>/subject/<int:subject_id>/study-materials/<str:module_name>',views.module,name="module"),
    path('class/<int:class_id>/subject/<int:subject_id>/study-materials/<str:module_name>/add-material',views.add_materials,name="add_note"),
    path('class/<int:class_id>/subject/<int:subject_id>/study-materials/<str:module_name>/edit-material/<int:material_id>',views.edit_materials,name="edit_materials"),
    path('class/<int:class_id>/subject/<int:subject_id>/study-materials/<str:module_name>/remove-material/<int:material_id>',views.remove_materials,name="remove_materials"),

    path('view-materials',views.view_materials,name="view_materials"),
    path('list-materials',views.list_materials,name="list_materials"),


]