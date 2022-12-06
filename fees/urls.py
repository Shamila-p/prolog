from django.urls import path
from . import views

urlpatterns = [
    path('display-fee',views.display_fee,name="display_fee"),
    path('add-fee',views.add_fee,name="add_fee"), 
    path('edit-fee/<int:fee_id>',views.edit_fee,name="edit_fee"),
    path('remove-fee/<int:fee_id>',views.remove_fee,name="remove_fee"),


     path('student-fee',views.student_fee,name="student_fee"),
    path('payment/<int:payment_id>',views.payment,name="student_fee"),

    path('sms',views.sms,name="sms"),

]