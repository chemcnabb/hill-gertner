# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ProtectedPage, ImageGallery, PDFpage, Image
# Register your models here.




class ProtectedPageAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProtectedPage, ProtectedPageAdmin)



class ImageInline(admin.TabularInline):
    model = Image
    ordering = ("order",)

class GalleryPageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'parent_page', 'order')
    list_editable = ['parent_page', 'order', ]
    fieldsets = (
        ('Page info', {
            'fields': ('parent_page', "slug")
        }),
        ('Page Content', {
            'fields': ('heading', 'subheading', 'paragraph'),
        })
    )
    inlines = (ImageInline,)
admin.site.register(ImageGallery, GalleryPageAdmin)

class PDFPageAdmin(admin.ModelAdmin):
    list_display = ('heading', 'parent_page', 'order')
    list_editable = ['parent_page', 'order',]
    fieldsets = (
        ('Page info', {
            'fields': ('parent_page', "slug")
        }),
        ('Page Content', {
            'fields':('heading', 'subheading','paragraph'),
        }),
        ('Presentation', {
            'fields': ('pdf',)
        }),
    )
admin.site.register(PDFpage, PDFPageAdmin)


