# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import redirect, render

from list.models import Item


def index(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/todolist')

    items = Item.objects.all()
    return render(request, 'todolist.html', {'items': items})
