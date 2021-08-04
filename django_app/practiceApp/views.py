from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def practice_page(request):
    #return HttpResponse("<h1>Hello Tanbir</h1>")

    return render(request, 'main/index2.html')

@csrf_exempt
def with_values2(request):
   
        first_form=request.POST["do_it"]
        print(first_form)
 
        return render(request, 'main/index2.html')

@csrf_exempt
def with_values1(request):
   
        first_form2=request.POST["the_send_text"]
        print(first_form2)
        
        return render(request, 'main/index2.html')
        

