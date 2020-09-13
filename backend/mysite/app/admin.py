from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
# Register your models here.
from .models import Condidat
# admin.site.register(Condidat)

class AccountAdmin(admin.ModelAdmin):
    List_display=("first_name","last_name","e_mail","birthday","cv","expirience_years_nbr", "availablity","confirmation")
    search_fields=("first_name","last_name","e_mail")
    filter_horizontal=()
    list_filter=("first_name","last_name","e_mail","birthday","confirmation")
    fielsets=()

admin.site.register(Condidat,AccountAdmin)
