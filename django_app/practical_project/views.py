from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from .models import practical_p

@csrf_exempt
def practical(request):
    return render(request,"project/pro.html")

Names=[]
Ages=[]

def loop():
    for [namer, ager] in zip(Names, Ages):
        print("Name: ", namer)
        print("Age: ", ager)


@csrf_exempt
def warning(request):
    namex = request.POST["Name"]
    print(namex)
    Names.append(namex)
    Agex=request.POST["Age"]
    print(Agex)
    Ages.append(Agex)
    loop()

    obj= practical_p.objects.create(name=namex, age=Agex)

    print(obj)
    print("object length : ", practical_p.objects.all().count())
    
    return render(request, "project/pro.html", {'names': Names, 'Ages': Ages})
    
