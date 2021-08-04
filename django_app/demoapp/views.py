from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.utils import timezone

from demoapp.models import Todo

def home(request):
      return render(request,'main/index.html')



@csrf_exempt
def new_build(request):
      posting_item2 = request.POST["do_it"]
      print(posting_item2)
      the_date = timezone.now()
      create_object = Todo.objects.create(add_date=the_date, text=posting_item2)
      
      return render(request, 'main/index.html')
      print(create_object)
      print(create_object.id)
      #add_todo(request)


@csrf_exempt
def add_todo(request):
    #print(request.POST)
    the_date = timezone.now()
    #return render(request, 'main/index.html')

    posting_item = request.POST["the_send_text"]

    print(posting_item)

    print(the_date)
    #new_build(request)
    return render(request, 'main/index.html')
