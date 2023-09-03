from django.http import HttpResponse
from django.shortcuts import render




def index(request): # HttpRequest
    return HttpResponse("Page app robots.")





def categories(request, cat_id):
    return HttpResponse(f"<h1>Notes by category</h1><p>id: {cat_id}</p>")




def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Notes by category</h1><p>slug: {cat_slug}</p>")




def archive(request, year):
    return HttpResponse(f"<h1>Archive by years</h1><p>{year}</p>")
