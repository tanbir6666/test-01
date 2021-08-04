from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.signUp, name="sign up page"),
    path("form_submit/", views.form_submit, name="form submit"),
    path("form_submit/delete/<int:user_id>/", views.delete_user, name="delete user"),
    path("form_submit/log_out/", views.logOut, name="log_out"),
    path("form_submit/save/<int:user_id>/", views.saves, name="save id" ),
    path("form_submit/undo/", views.undo, name="undo")
]

