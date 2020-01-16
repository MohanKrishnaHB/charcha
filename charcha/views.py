from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse
from django.shortcuts import render

def health_check(request):
    return HttpResponse("OK", status=200)

def welcome_page(request):
    return render(request, "welcome.html")