from django.shortcuts import render
from django.http import HttpResponse


def vista1(request):
    return HttpResponse("<h1>Vista 1</h1>")

def vista2(request):
    return HttpResponse("<h1>Vista 2</h1>")