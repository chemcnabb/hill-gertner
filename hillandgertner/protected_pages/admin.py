# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProtectedPage, ImageGallery, PDFpage, Image
# Register your models here.








class ImageInline(admin.TabularInline):
    model = Image

class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'order')
    list_editable = ['order',]
    fieldsets = (
        ('Page info', {
            'fields': ('page_name', "slug")
        }),

    )
    inlines = (ImageInline,)
admin.site.register(ImageGallery, GalleryPageAdmin)

class PDFPageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'order')
    list_editable = ['order',]
    fieldsets = (
        ('Page info', {
            'fields': ('page_name', "slug")
        }),
        ('Presentation', {
            'fields': ('pdf',)
        }),
    )
admin.site.register(PDFpage, PDFPageAdmin)


