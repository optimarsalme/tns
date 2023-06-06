from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django.contrib.auth.models import User
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display        = ('email', 'userName', 'firstName', 'lastName',)
    list_display_links  = ('email', 'userName',)
    readonly_fields     = ('last_login', 'date_joined',)
    ordering            = ('date-joined',)