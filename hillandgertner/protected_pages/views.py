# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from hillandgertner.pages.models import Page
debug=False
if not debug:
    from hillandgertner.page_globals.models import Globals


