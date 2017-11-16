# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Globals
# Register your models here.
class GlobalsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Globals, GlobalsAdmin)
# Register your models here.
