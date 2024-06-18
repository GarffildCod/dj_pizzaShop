from django.contrib import admin
from django.contrib.admin import AdminSite

from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin


class MyAdminSite(AdminSite):
    site_header = "Simiram - Админ"


admin_site = MyAdminSite(name='admin')


admin_site.register(User, UserAdmin)
admin_site.register(Group)