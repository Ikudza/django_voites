# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from clients import models

class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "age", "birthday", "voite")
    search_fields = ["name", "surname"]
admin.site.register(models.Client, ClientAdmin)
