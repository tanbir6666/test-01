from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.index, name="index page"),
    path("clever/", views.index, name="index page"),
    path("registerUser/registrationUser/", views.signUp, name="After Registration page"),
    path("registerUser/registrationUser/log_out/", views.logOut, name="log out")





]
