from django.urls import path
from . import views

urlpatterns = [
    path('profile',views.profile,name="profile"),
    path('profile/edit-profile',views.edit_profile,name="edit_profile"),
    path('profile/change-password', views.change_password, name='change_password'),


    path('list-teachers',views.list_teachers,name="list_teachers"),
    path('add-teachers',views.add_teachers,name="add_teachers"),
    path('edit-teacher/<int:user_id>',views.edit_teacher,name="edit_teacher"),
    path('approve-teacher/<int:user_id>',views.approve_teacher,name="approve_teacher"),
    path('remove-teacher/<int:user_id>',views.remove_teacher,name="remove_teachers"),

    path('list-students',views.list_students,name="list_students"),
    path('add-student',views.add_student,name="add_student"), 
    path('edit-student/<int:user_id>',views.edit_student,name="edit_student"),
    path('approve-student/<int:user_id>',views.approve_student,name="approve_student"),
    path('remove-student/<int:user_id>',views.remove_student,name="remove_student"),

    path('edit-profile/request/<int:user_id>',views.edit_profile_request,name="edit_profile_request"),
    path('accept-request/<int:user_id>',views.accept_request,name="accept_request"),
    path('decline-request/<int:user_id>',views.decline_request,name="decline_request"),
]