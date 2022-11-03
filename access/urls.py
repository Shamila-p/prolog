from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('forgot-password', views.forgot_password, name="forgot_password"),
    path('reset-password/<str:reset_id>', views.reset_password, name="reset_password"),
]
