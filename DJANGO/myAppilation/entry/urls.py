from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.entryPage, name="entry page"),
    path("send/", views.addEntryData, name="send user data"),
    path("entry/", views.entryview),
    path("entry/delete/<int:user_id>/", views.Delete_id, name="delete user"),
    path("entry/undo/", views.undoDELETE, name="undo"),
    path("entry/log_out/", views.logOut, name="log_out"),

]
