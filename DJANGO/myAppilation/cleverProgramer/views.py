from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserDatabase, SearchHistory, SearchData
from django.views.decorators.csrf import csrf_exempt

all_ready_in = False


def logINCheck(request):
    global all_ready_in
    try:
        Cookie_name = request.COOKIES.get("name")
        Cookie_email = request.COOKIES.get("email")
        Cookie_author = request.COOKIES.get("author")
        len(Cookie_name)
        len(Cookie_email)
        len(Cookie_author)
        try:
            user_log = UserDatabase.objects.get(userAuthor=Cookie_author)
            print(user_log)
            print(user_log)
            all_ready_in = True
            return render(request, "index_cl/registerUser/registrationUser.html")

        except:
            print("No Author Found with this name, Fake Cookie")
            response = HttpResponseRedirect("/clever/")
            try:
                print("WE are Deleting Fake Cookie")
                response.delete_cookie("name")
                response.delete_cookie("email")
                response.delete_cookie("author")
                return response
            except:
                return response

    except:
        all_ready_in = False
        print("no Cookie Found")
        response = HttpResponseRedirect("/clever/")
        try:
            print("WE are Deleting Fake Cookie")
            response.delete_cookie("name")
            response.delete_cookie("email")
            response.delete_cookie("author")
            return response
        except:
            return response


def logOut(request):
    global all_ready_in
    response = HttpResponseRedirect("/clever/")
    try:
        response.delete_cookie("name")
        response.delete_cookie("email")
        response.delete_cookie("author")
        all_ready_in = False
        return response
    except:
        return response
    finally:
        print("log out successful")


# Create your views here.
def index(request):
    logINCheck(request)
    return render(request, "index_cl/index_cl.html")


def logIn(request):

    global all_ready_in
    try:
        Cookie_name = request.COOKIES.get("name")
        Cookie_age = request.COOKIES.get("email")
        Cookie_author = request.COOKIES.get("author")
        len(Cookie_name)
        len(Cookie_age)
        len(Cookie_author)
        all_ready_in = True
        logINCheck(request)
        return render(request, "index_cl/registerUser/registrationUser.html")
    except:
        return HttpResponseRedirect("/clever/")


@csrf_exempt
def signUp(request):
    global all_ready_in
    try:
        user_name = request.POST["name"]

        user_password = request.POST["password"]
        user_email = request.POST["email"]
        Author = str(user_email) + str(user_password)
        print("all fields Found !")
        print("Checking For Duplicates")
        try:

            Duplicate = UserDatabase.objects.get(userName=user_name)
            print("Name is already exist")
            all_ready_in = False
            return HttpResponseRedirect("/clever/")
        except:

            try:
                UserDatabase.objects.create(userName=user_name,
                                            userEmail=user_email, userPassword=user_password, userAuthor=Author)
                print("insert Table successful")
                response = render(request, "index_cl/registerUser/registrationUser.html")
                response.set_cookie("name", user_name)
                response.set_cookie("email", user_email)
                response.set_cookie("author", Author)
                all_ready_in = True
                return response

            except:
                print("unable to Set data on the UserData table")
                return HttpResponseRedirect("/clever/")



    except:
        print("Please Enter all the fields")
        return HttpResponseRedirect("/clever/")
