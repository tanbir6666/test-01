import pandas
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, cookie
from django.views.decorators.csrf import csrf_exempt
from .models import Entry, DeleteEntry
import datetime

today = datetime.date.today()
tab = None
entry_database = {
    "names": [],
    "ages": [],
    "gender": [],
    "time": [],
}

tmp_database = {
    "name": '',
    "age": '',
    'Gender': '',
}
errors = ''
massage = "WELCOME TO MY SITE"


def Checklog(request):
    c_user = request.COOKIES.get("Name")
    c_age = request.COOKIES.get("Age")
    c_gender = request.COOKIES.get("Gender")
    if c_user is None or c_age is None or c_gender is None:
        return False
    else:
        return True


# Create your views here.
def entryPage(request):
    global massage, tmp_database, errors
    try:

        c_user = request.COOKIES.get("Name")
        c_age = request.COOKIES.get("Age")
        c_gender = request.COOKIES.get("Gender")
        if c_user is None or c_age is None or c_gender is None:
            return render(request, "index/index.html",
                          {"massages": massage, "name": tmp_database["name"], "age": tmp_database["age"],
                           "gender": tmp_database["Gender"], "errors": errors})
        else:
            return HttpResponseRedirect("/entry/")

    except:

        return render(request, "index/index.html",
                      {"massages": massage, "name": tmp_database["name"], "age": tmp_database["age"],
                       "gender": tmp_database["Gender"], "errors": errors})


@csrf_exempt
def addEntryData(request):
    global entry_database, tab, massage, today, tmp_database, errors
    try:
        posts = [request.POST.get("name"), request.POST.get(
            "age"), request.POST.get("gender")]



    except:
        posts = False
    if posts:

        name = request.POST.get("Name")
        age = request.POST.get("Age")
        try:
            age_type = int(age)
        except:
            age_type = None
        genders = request.POST.get("Gender")
        if len(name) < 3:
            errors = 0
            massage = "please enter your name more than 2 charectars"
            print("61")
            return HttpResponseRedirect("/")

        else:
            tmp_database["name"] = name
            if age_type is None:
                print("66")
                errors = 1
                massage = "please enter your Age. that should be a number"
                return HttpResponseRedirect("/")
            else:
                tmp_database["age"] = age
                if genders == "Male" or genders == "Female":
                    print(name, age, genders)
                    tmp_database["Gender"] = genders
                    try:
                        Entry.objects.create(names=name, ages=age, gender=genders)
                        print("data submitted")
                    except:
                        print("unable to Set entrys")
                    finally:
                        tab = pandas.DataFrame({
                            "Name": entry_database["names"],
                            "Age": entry_database["ages"],
                            "Gender": entry_database["gender"],
                            "time": entry_database["time"],
                        })

                        response = HttpResponseRedirect("/entry/")
                        response.set_cookie("Name", name)
                        response.set_cookie("Age", age)
                        response.set_cookie("Gender", genders)
                        print("88")
                        return response


                else:
                    errors = 2
                    print(genders)
                    print("78")
                    massage = "please Select your Gender "
                    return HttpResponseRedirect("/")



    else:
        print("91")
        massage = "please enter all the inputs"
        return HttpResponseRedirect("/")


@csrf_exempt
def entryview(request):
    try:
        c_user = request.COOKIES.get("Name")
        c_age = request.COOKIES.get("Age")
        c_gender = request.COOKIES.get("Gender")
        if c_user is None or c_age is None or c_gender is None:
            return HttpResponseRedirect("/")
        else:
            global entry_database, tab
            entry_database = {
                "names": [],
                "ages": [],
                "gender": [],
                "time": [],
            }

            table = Entry.objects.all().order_by('-id')

            for da in table:
                entry_database["names"].append(da.names)
                entry_database["ages"].append(da.ages)
                entry_database["gender"].append(da.gender)
                entry_database["time"].append(da.entryTime)
                print(da.names)
            print(type(table))
            tab = pandas.DataFrame({
                "Name": entry_database["names"],
                "Age": entry_database["ages"],
                "Gender": entry_database["gender"],
                "time": entry_database["time"],
            })

            print(tab)
            return render(request, "index/Entry_data/entry_data.html",
                          {"entry": table, "name": c_user, "age": c_age, "gender": c_gender, "massages": massage})
    except:
        return HttpResponseRedirect("/")


def Delete_id(request, user_id):
    if Checklog(request):
        try:
            the_user = Entry.objects.get(id=user_id)
            try:
                user_name = the_user.names
                user_age = the_user.ages
                user_gender = the_user.gender
                user_ids = the_user.id
                user_create = the_user.entryTime
                print(user_name, user_age, user_gender)
                try:
                    DeleteEntry.objects.create(
                        entryID=user_ids, names=user_name, ages=user_age, gender=user_gender, createEntry=user_create)
                    try:
                        Entry.objects.get(id=user_id).delete()
                        return HttpResponseRedirect("/entry/")
                    except:
                        print("Unable to DELETE : 3")
                        return HttpResponseRedirect("/entry/")

                except:
                    print("Unable to DELETE : 2")
                    return HttpResponseRedirect("/entry/")

            except:
                print("Unable to DELETE : 1")
                return HttpResponseRedirect("/entry/")
        except:
            print("Unable to DELETE")
            return HttpResponseRedirect("/entry/")
    else:
        return HttpResponseRedirect("/")


def undoDELETE(request):
    if Checklog(request):
        try:
            DeleteEntry.objects.all().order_by("id")

            undo_id = DeleteEntry.objects.latest("id")

            Entry.objects.create(id=undo_id.entryID,
                                 names=undo_id.names, ages=undo_id.ages, gender=undo_id.gender,
                                 entryTime=undo_id.entryTime)

            DeleteEntry.objects.get(id=undo_id.id).delete()
            return HttpResponseRedirect("/entry/")
        except:
            print("Unable to UNDO")
            return HttpResponseRedirect("/entry/")
    else:
        return HttpResponseRedirect("/")


def logOut(request):
    global massage, tmp_database, errors
    try:
        massage = "Welcome To my site"
        tmp_database["name"] = ''
        tmp_database["age"] = ''
        tmp_database["Gender"] = ''
        errors = ''
        response = HttpResponseRedirect("/")
        response.delete_cookie("Name")
        response.delete_cookie("Age")
        response.delete_cookie("Gender")
        return response
    except:
        return HttpResponseRedirect("/entry/")
