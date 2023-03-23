from django.contrib import admin
from .models import (
    person,
    data,
    nubm
)

class databaseadmin1(admin.ModelAdmin):
    list_display = ['userid', 'username', 'password',]

class databaseadmin2(admin.ModelAdmin):
    list_display = ['userid', 'froms', 'to']

class databaseadmin3(admin.ModelAdmin):
    list_display = ['userid', 'nubm']

admin.site.register(person,  (databaseadmin1))
admin.site.register(data,  (databaseadmin2))
admin.site.register(nubm,  (databaseadmin3))
