 # todo/admin.py

from django.contrib import admin
from .models import Tjournal # add this

class TjournalAdmin(admin.ModelAdmin):  # add this
    list_display = ('stock', 'entryprice', 'exitprice') # add this

# Register your models here.
admin.site.register(Tjournal, TjournalAdmin) # add this