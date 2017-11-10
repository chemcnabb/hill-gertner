from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify
# Create your models here.
class Page(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    background_image = models.ImageField(blank=True, null=True)
    # header = models.CharField(max_length=500,blank=True, null=True)
    # subheader = models.CharField(max_length=500,blank=True, null=True)
    page_name = models.CharField(max_length=500,blank=False, null=True)
    num_columns = models.IntegerField(blank=True, null=True)

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
