# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User

def contatti(request):
    return render(request, "contatti.html")

def profile(request):
    args = {'user':request.user}
    return render(request, 'profile.html', args)