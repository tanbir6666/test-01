from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import show_it

from .models import text_massage
from .models import LinkElements
from bs4 import BeautifulSoup
import requests as rq

alerts = None
search_values = ""


# Create your views here.


@csrf_exempt
def show(request):
    global alerts, search_values
    if alerts is None:
        alerts = "Ready to insert Data"
    showItems = show_it.objects.all().order_by("-id")
    # giving a Negative Sign (-) Will Reverse Order on the items
    massages = text_massage.objects.all().order_by("id")

    links_elements_each = LinkElements.objects.all().order_by("-id")
    return render(request, "page/page.html",
                  {"items": showItems, "alerts": alerts, "text_massage": massages, "search_text": links_elements_each})


@csrf_exempt
def gowithData(request):
    global alerts

    names = request.POST["name"]

    ages = request.POST["age"]
    rolls = request.POST["roll"]
    if len(names) > 0 and len(ages) > 0 and len(rolls) > 0:

        if names.isnumeric():
            print("Name is a Number")
            alerts = "Please Enter a Name Not a Number"
        else:
            print("its a string")
            alerts = "Data Has been insert correctly"
            print(names, ages, rolls)
            adding_data = show_it.objects.create(name=names, age=ages, roll=rolls)

            print("object length : ", show_it.objects.all().count())
            print(adding_data)
    else:
        alerts = "Please Enter All Inputs"
    return HttpResponseRedirect("/")


@csrf_exempt
def delete(request, table_id):
    print(table_id)
    show_it.objects.get(id=table_id).delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def massage(request, name):
    user_name = name
    user_massage = request.POST["massage"]
    give_massage = text_massage.objects.create(NAME=user_name, MASSAGE=user_massage)
    print(give_massage)
    return HttpResponseRedirect("/")


@csrf_exempt
def delete_massage(request, delete_massage_id):
    id_m = delete_massage_id
    text_massage.objects.get(id=id_m).delete()
    return HttpResponseRedirect("/")


@csrf_exempt
def searching(request):
    global search_values
    search_text = request.POST["search_text"]
    the_search_rquest = rq.get(search_text)
    page_elements = BeautifulSoup(the_search_rquest.content, "html.parser")
    search_values_ = page_elements.find("html")
    to_str_search_values_ = str(search_values_)
    LinkElements.objects.create(links=to_str_search_values_)

    # print(len(search_values_))
    # search_values__ = search_values_.select("a")
    #
    # for search_val__ in search_values__:
    #     link_ = str(search_val__)
    #     LinkElements.objects.create(links=link_)

    return HttpResponseRedirect("/")


@csrf_exempt
def delete_links(request, link_id):
    LinkElements.objects.get(id=link_id).delete()
    return HttpResponseRedirect("/")
