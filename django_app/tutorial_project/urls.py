from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path("", views.show, name="show"),
    url(r'add_data/', views.gowithData, name="data"),
    path('delete/<int:table_id>/', views.delete, name="delete"),
    path('send/<str:name>/', views.massage, name="massage"),
    path('delete_massage/<int:delete_massage_id>/', views.delete_massage, name="delete Massage"),
    path('searching/', views.searching, name="search"),
    path('delete_links/<int:link_id>/', views.delete_links, name="delete_link"),

]
