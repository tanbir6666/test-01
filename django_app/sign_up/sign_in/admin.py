from django.contrib import admin
from .models import UserTable, DeleteUser
# Register your models here.
admin.site.register(UserTable)
admin.site.register(DeleteUser)