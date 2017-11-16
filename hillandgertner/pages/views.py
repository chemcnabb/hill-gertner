# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from hillandgertner.pages.models import Page
from hillandgertner.page_globals.models import Globals

# Create your views here.
class IndexView(TemplateView):
    template_name = 'main.html'
    pages = Page.objects.order_by('-order')
    globals = Globals.objects.first()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pages'] = self.pages
        context['globals'] = self.globals
        return context
