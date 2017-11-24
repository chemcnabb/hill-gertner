from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from tinymce.models import HTMLField
import subprocess
from django.conf import settings
# Create your models here.
from django.template.defaultfilters import slugify
# Create your models here.
class Page(models.Model):
    date = models.DateTimeField(blank=True, null=True)

    heading_text_size = models.IntegerField(blank=False, null=True, default=10)
    heading_text_color = models.CharField(max_length=500, blank=False, null=True, default="#000")
    subheading_text_size = models.IntegerField(blank=False, null=True, default=10)
    subheading_text_color = models.CharField(max_length=500, blank=False, null=True, default="#000")
    body_text_size = models.IntegerField(blank=False, null=True, default=12)
    body_text_color = models.CharField(max_length=500, blank=False, null=True, default="#000")

    background_image = models.ImageField(blank=True, null=True)
    # header = models.CharField(max_length=500,blank=True, null=True)
    # subheader = models.CharField(max_length=500,blank=True, null=True)
    page_name = models.CharField(max_length=500,blank=False, null=True)
    num_columns = models.IntegerField(blank=True, null=True, default=12)
    text_format = models.CharField(max_length=500,blank=True, null=True, default="text-justify")

    copy = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    order = models.IntegerField(default=0)


    def __unicode__(self):
        return self.page_name or self.date



    def get_url(self):
        return "#%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.page_name)
        super(Page, self).save(*args, **kwargs)

# method for updating
@receiver(post_save, sender=Page, dispatch_uid="touch_tmp")
def touch_tmp(sender, instance, **kwargs):
     # print settings.BASE_DIR + "/tmp/restart.txt"
     subprocess.call(["touch", settings.BASE_DIR + "/tmp/restart.txt"])
