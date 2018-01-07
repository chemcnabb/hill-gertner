from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from tinymce.models import HTMLField
from hillandgertner.pages.models import Page
import subprocess
from django.conf import settings
# Create your models here.
from django.template.defaultfilters import slugify
# Create your models here.


PAGE_TYPES = (
    ('pdf', 'PDF File'),
    ('gallery', 'Gallery'),
)

class PDFManager(models.Manager):
    def get_queryset(self):
        return super(PDFManager, self).get_queryset().filter(
            type='pdf')

class GalleryManager(models.Manager):
    def get_queryset(self):
        return super(GalleryManager, self).get_queryset().filter(
            type='gallery')

class Image(models.Model):
    image = models.ImageField(blank=True, null=True)
    gallery = models.ForeignKey('ImageGallery', blank=True, null=True)



class ProtectedPage(models.Model):
    type = models.CharField(max_length=7, choices=PAGE_TYPES)
    date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    parent_page = models.ForeignKey(Page, null=True, blank=True)
    background_image = models.ImageField(blank=True, null=True)
    heading = models.CharField(max_length=500, blank=False, null=True)
    subheading = models.CharField(max_length=500, blank=True, null=True)
    paragraph = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    order = models.IntegerField(default=0)
    pdf = models.FileField(blank=True, null=True)

    def __unicode__(self):
        return self.heading or self.date

    def get_url(self):
        return "#%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.heading)
        super(ProtectedPage, self).save(*args, **kwargs)

class PDFpage(ProtectedPage):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'pdf'
        super(PDFpage, self).__init__(*args, **kwargs)
    objects = PDFManager()
    class Meta:
        proxy = True
        verbose_name = "PDF page"
        verbose_name_plural = "PDF pages"

class ImageGallery(ProtectedPage):
    def __init__(self, *args, **kwargs):
        self._meta.get_field('type').default = 'gallery'
        super(ImageGallery, self).__init__(*args, **kwargs)
    objects = GalleryManager()
    class Meta:
        proxy = True
        verbose_name = "Image gallery"
        verbose_name_plural = "Image galleries"



# method for updating
@receiver(post_save, sender=ProtectedPage, dispatch_uid="touch_tmp")
def touch_tmp(sender, instance, **kwargs):
     # print settings.BASE_DIR + "/tmp/restart.txt"
     subprocess.call(["touch", settings.BASE_DIR + "/tmp/restart.txt"])
