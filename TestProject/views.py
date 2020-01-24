from django.shortcuts import render
from django.http import HttpResponse
from .models import Name


def index(request):
    return HttpResponse("<h2>You have reached the homepage</h2>")