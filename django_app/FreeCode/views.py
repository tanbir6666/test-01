from django.shortcuts import render

from  django.http import HttpResponse

# Create your views here.

def codes(request):
    #return HttpResponse("<h1>Hello From FreeCode</h1>")
    return render(request, "main/index of freecode.html")




