# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    text = """
    <h1> Hello World! <h1>
    """
    return HttpResponse(text)


def home(request):
    return render(request, 'index.html')
