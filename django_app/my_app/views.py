from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserTable as Ut
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.`

alert = "welcome"
user_name = ''
user_mail = ''
user_pass = ''
sign = False


def runapp(request):
    global alert
    return render(request, "index/index.html", {"alert": alert})


@csrf_exempt
def signup(request):
    global alert, sign

    user_name = request.POST.get("user_name")
    user_mail = request.POST.get("email")
    user_pass = request.POST.get("user_pass")

    if sign is False:
        if len(user_name) > 3 and len(user_mail) > 9 and len(user_pass) > 4:
            sign = True
            print(sign)
            print(user_name, user_mail, user_pass)
            Ut.objects.create(name=user_name, email=user_mail, password=user_pass)
            view_table = Ut.objects.all().order_by("-id")
            return render(request, "index/sign_up/sign_up.html", {"name": user_name, "email": user_mail,
                                                                  "password": user_pass, "user_data": view_table})

        else:
            alert = "Please Enter All The Inputs"
            return HttpResponseRedirect("/")
    else:
        view_table = Ut.objects.all().order_by("-id")
        return render(request, "index/sign_up/sign_up.html", {"name": user_name, "email": user_mail,
                                                              "password": user_pass, "user_data": view_table})


@csrf_exempt
def signup_(request):
    global user_name, user_mail, user_pass
    if user_name is None or user_mail is None or user_pass is None:
        user_name = "ID  has  Deleted"
        user_mail = "NONE"
        user_pass = "NONE"
    view_table = Ut.objects.all().order_by("-id")
    return render(request, "index/sign_up/sign_up.html", {"name": user_name, "email": user_mail,
                                                          "password": user_pass, "user_data": view_table})


@csrf_exempt
def delete(request, user_id):
    global user_name, user_mail, user_pass
    Ut.objects.get(id=user_id).delete()

    return HttpResponseRedirect("/signup_/")


@csrf_exempt
def sign_up(request, user_id):
    global user_name, user_mail, user_pass
    if user_name is None or user_mail is None or user_pass is None:
        user_name = str(user_id) + " NO ID  has  Deleted"
        user_mail = "NONE"
        user_pass = "NONE"
    view_table = Ut.objects.all().order_by("-id")
    return render(request, "index/sign_up/sign_up.html",
                  {"name": user_name, "email": user_mail, "password": user_pass, "user_data": view_table})


@csrf_exempt
def logOut(request):
    global sign
    sign = False
    print(sign)
    return HttpResponseRedirect("/")


import requests as rq
from bs4 import BeautifulSoup as Bu


def katmovie(request):
    return render(request, "index/sign_up/katmovie/katmovie.html")


@csrf_exempt
def kat_search(request):
    has_search_element = None
    try:
        has_search_element = request.POST.get("search_text")
    except:
        has_search_element = None
    finally:
        print("Gone from here")

    if has_search_element:

        page_url = rq.get("http://katmoviehd.to/?s=" + str(has_search_element))
        get_page = Bu(page_url.content, "html.parser")
        get_resent_posts = get_page.find(class_="recent-posts")

        return render(request, "index/sign_up/katmovie/katmovie.html", {"page_info": get_resent_posts})
    else:
        return HttpResponseRedirect("/signup_/katmovie/")
        #return render(request, "index/sign_up/katmovie/katmovie.html")
