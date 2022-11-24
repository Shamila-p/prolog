from django.urls import path
from . import views

urlpatterns = [
    path('class/<int:class_id>/subject/<int:subject_id>/attendence',views.attendence,name="attendence"),
    path('add-attendence',views.add_attendence,name="add_attendence"),
]