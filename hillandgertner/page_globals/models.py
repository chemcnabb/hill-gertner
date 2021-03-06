# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db.models.signals import post_save
from django.dispatch import receiver
import subprocess
from django.db import models
from django.conf import settings

# Create your models here.
class Globals(models.Model):
    header_height = models.CharField(max_length=500, blank=False, null=True, default="25.8")
    page_background_color = models.CharField(max_length=500, blank=False, null=True, default="rgba(89,89,89,0.1)")
    heading_text_size = models.IntegerField(blank=False, null=True, default=10)
    heading_text_color = models.CharField(max_length=500, blank=False, null=True, default="#000")
    body_text_size = models.IntegerField(blank=False, null=True, default=12)
    body_text_color = models.CharField(max_length=500, blank=False, null=True, default="#000")

# method for updating
@receiver(post_save, sender=Globals, dispatch_uid="touch_tmp")
def touch_tmp(sender, instance, **kwargs):
    # print settings.BASE_DIR + "/tmp/restart.txt"
    subprocess.call(["touch", settings.BASE_DIR + "/tmp/restart.txt"])
