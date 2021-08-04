from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url



from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', views.practical,name="Practical Project"),

    url(r'warning/', views.warning, name="form"),
    #path('warning/', views.warning, name="form")
]
