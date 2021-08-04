from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from bs4 import BeautifulSoup as Bu
import  requests as rq
import re
from django.views.decorators.csrf import  csrf_exempt

# Create your views here.


def home(request):
    return render(request, "search/offlineSearch.html")
    

@csrf_exempt
def search(request):
    #data = Bu(stringData.content,"html.parser")
    mains=stringData.search(class_="main")
    print(mains)