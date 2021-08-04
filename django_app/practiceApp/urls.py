
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns=[
  
    url(r'^admin/',admin.site.urls),
     
    #url(r"^$",views.practice_page,name="Home Page"),
    path('', views.practice_page, name='home_page'),
    url(r'new_build/',views.with_values2,name="new to do"),
    url(r'add_todo/',views.with_values1,name="To Do App"),
    
]
