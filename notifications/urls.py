from django.urls import path
from . import views

urlpatterns = [
    path('complaint',views.send_complaint,name="send_complaint"),
]