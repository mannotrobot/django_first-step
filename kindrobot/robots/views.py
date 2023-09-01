from django.http import HttpResponse
from django.shortcuts import render




def index(request): # HttpRequest
    return HttpResponse("Page app robots.")





def categories(request):
    return HttpResponse("<h1>Notes by category</h1>")
