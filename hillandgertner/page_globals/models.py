# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Globals(models.Model):
    header_height = models.CharField(max_length=500, blank=False, null=True, default="25.8")
    page_background_color = models.CharField(max_length=500, blank=False, null=True, default="rgba(89,89,89,0.1)")
