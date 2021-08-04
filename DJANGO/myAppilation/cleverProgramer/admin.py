from django.contrib import admin

# Register your models here.

from .models import UserDatabase, SearchHistory,SearchData
# Register your models here.
admin.site.register(UserDatabase)
admin.site.register(SearchHistory)
admin.site.register(SearchData)