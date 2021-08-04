from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserTable, DeleteUser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
form_alert = ""
delete_global = ""
user_table = None
logged_in = False
user_static = {
    "name": "",
    "email": "",
    "password": "",

}
just_deleted = []


def signUp(request):
    global form_alert, user_static
    # return HttpResponse("<h1>Hello Tanbir </h1>")
    return render(request, "main/index.html", {"alert": form_alert, "user": user_static})


@csrf_exempt
def form_submit(request):
    global form_alert, user_table, logged_in, delete_global, user_static
    got_values = False
    if logged_in is False:
        try:
            got_values = [request.POST.get("name"), request.POST.get("email"), request.POST.get("password")]

        except:
            got_values = False

        if got_values:

            try:
                name = got_values[0]
                email = got_values[1]
                password = got_values[2]

            except:
                name = False
                email = False
                password = False

            finally:
                print("PROCESS COMPLETE")

            if name and email and password:

                if len(password) < 8:
                    user_static["name"] = name
                    user_static["email"] = email
                    user_static["password"] = password
                    print(len(password), password)
                    form_alert = "Please Enter Minimum 8 Digit Password"
                    return HttpResponseRedirect("/")

                else:
                    print(len(password), password)
                    UserTable.objects.create(names=name, emails=email, passwords=password)
                    user_table = UserTable.objects.all().order_by("-id")
                    logged_in = True
                    return render(request, "main/page/signup.html", {"table": user_table})
            else:
                return HttpResponseRedirect("/")
        else:
            form_alert = "Please Enter All the inputs"
            return HttpResponseRedirect("/")
    else:

        return render(request, "main/page/signup.html", {"table": user_table, "Notification": delete_global})


@csrf_exempt
def delete_user(request, user_id):
    global just_deleted

    target_user = UserTable.objects.get(id=user_id)
    name = target_user.names
    notification = str(name) + "'s id has Deleted"
    just_deleted.append(int(user_id))
    DeleteUser.objects.create(names=target_user.names, emails=target_user.emails,
                              passwords=target_user.passwords, id=target_user.id)

    global delete_global, user_table
    delete_global = notification
    UserTable.objects.get(id=user_id).delete()
    user_table = UserTable.objects.all().order_by("-id")

    return HttpResponseRedirect("/form_submit/")


def logOut():
    global logged_in
    logged_in = False
    return HttpResponseRedirect("/")


@csrf_exempt
def saves(request, user_id):
    global user_table

    get_user = UserTable.objects.get(id=user_id)
    print(request.POST.get("name"))
    print(request.POST.get("email"))
    print(request.POST.get("password"))
    get_user.names = request.POST.get("name")
    get_user.emails = request.POST.get("email")
    get_user.passwords = request.POST.get("password")
    get_user.save()
    user_table = UserTable.objects.all().order_by("-id")
    return HttpResponseRedirect("/form_submit/")


@csrf_exempt
def undo(request):
    global just_deleted, user_table, delete_global
    print(just_deleted)

    try:
        The_id = int(just_deleted[-1])
    except:
        The_id = False

    try:
        last_delete = DeleteUser.objects.get(id=The_id)
    except:
        last_delete = False
    if last_delete:
        UserTable.objects.create(names=last_delete.names, emails=last_delete.emails, passwords=last_delete.passwords,
                                 id=last_delete.id)
        DeleteUser.objects.get(id=last_delete.id).delete()
        just_deleted.pop()
        user_table = UserTable.objects.all().order_by("-id")
        delete_global = "ID No: " + str(last_delete.id) + " has restored"
    else:
        print(just_deleted)
        try:
            print(just_deleted[-1])
        except:
            print("just_deleted[-1] dose not exist")
        print("ID NOT Found")
        delete_global = "ID NOT Found"
    return HttpResponseRedirect("/form_submit/")
