from django.urls import path
from . import views

urlpatterns = [
    path('complaint',views.complaint,name="complaint"),
    path('display-complaint',views.display_complaint,name="display_complaint"),
    path('no-complaint',views.no_complaint,name="no_complaint"),

    path('notification',views.notification,name="notification"),
    path('display-notification',views.display_notification,name="display_notification"),


]