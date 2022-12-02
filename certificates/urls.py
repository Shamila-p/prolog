from django.urls import path
from . import views

urlpatterns = [
    path('list-certificates',views.list_certificates,name="list_certificates"),
    path('add-certificate',views.add_certificate,name="add_certificates"),
    path('edit-certificate/<int:certificate_id>',views.edit_certificate,name="edit_certificate"),
    path('remove-certificate/<int:certificate_id>',views.remove_certificate,name="remove_certificate"),

    path('view-certificates',views.view_certificates,name="view_certificates"),


]