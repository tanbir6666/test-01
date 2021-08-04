from django.conf.urls import url
from django.contrib import admin
#from django.urls import path
from . import views

urlpatterns = [
     #path('', views.home, name='home-page'),
     url(r'^admin/',admin.site.urls),
     
     url(r"^$",views.home,name="Home Page"),
     url(r'new_build/',views.new_build,name="new to do"),
     url(r'add_todo/',views.add_todo,name="To Do App"),
     

]
