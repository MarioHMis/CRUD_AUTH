from django.shortcuts import render
from django.http import HttpResponse

def hellowworl(request):
    return HttpResponse(' Hello world')