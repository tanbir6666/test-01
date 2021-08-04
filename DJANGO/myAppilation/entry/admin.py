from django.contrib import admin

# Register your models here.

from .models import Entry, DeleteEntry
# Register your models here.
admin.site.register(Entry)
admin.site.register(DeleteEntry)
