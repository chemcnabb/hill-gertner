# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from .models import Page

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'main.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Page.objects.order_by('-pub_date')[:5]
