from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import CuponDescuento, Profile


class UserProfileInline(admin.StackedInline):
    model = Profile
    filter_horizontal = ('cupones_descuento',)


class CustomUserAdmin(UserAdmin):
    inlines = [UserProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(CuponDescuento)