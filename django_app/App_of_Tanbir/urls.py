from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.home,name="Home page" ),
    #path('', include('demoapp.urls'))
]
