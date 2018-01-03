# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Page
from hillandgertner.protected_pages.models import ImageGallery, PDFpage



class ImageGalleryManagerInline(admin.TabularInline):
  model=ImageGallery
  fields=("page_name","type")
  readonly_fields=("page_name","type")
  max_num=0


class PDFPageManagerInline(admin.TabularInline):
  model=PDFpage
  fields=("page_name","type")
  readonly_fields=("page_name","type")
  max_num=0


# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'order')
    list_editable = ['order',]
    inlines = [ImageGalleryManagerInline, PDFPageManagerInline]
admin.site.register(Page, PageAdmin)











