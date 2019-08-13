from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Index page</h1>")


def questions(request):
    return HttpResponse("<h1>Questions page</h1>")
