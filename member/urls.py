from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile,name="profile"),

    path('list-teachers',views.list_teachers,name="list_teachers"),
    path('add-teachers',views.add_teachers,name="add_teachers"),
    path('edit-teacher/<int:user_id>',views.edit_teacher,name="edit_teacher"),
    path('approve-teacher/<int:user_id>',views.approve_teacher,name="approve_teacher"),
    path('remove-teacher/<int:user_id>',views.remove_teacher,name="remove_teachers"),

    path('list-students',views.list_students,name="list_students"),
    path('add-student',views.add_student,name="add_student"), 
]