from django.urls import path
from . import views
urlpatterns= [
    path("",views.home, name=""),
    path("s/", views.getElements, name="search text"),

    
]