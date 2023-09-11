from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string



menu = ['about site', 'add notes', 'callback', 'enter']



data_db = [
    {'id': 1, 'title': 'T-800', 'content': 'Info T-800', 'is_pub': True},
    {'id': 2, 'title': 'T-1000', 'content': 'Info T-1000', 'is_pub': False},
    {'id': 3, 'title': 'Bander', 'content': 'Info Bander', 'is_pub': True},
]




def index(request): # HttpRequest
    data = {
        'title': 'main page',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'robots/index.html', context=data)




def about(request):
    return render(request, 'robots/about.html', {'title': 'About site'})




def categories(request, cat_id):
    return HttpResponse(f"<h1>Notes by category</h1><p>id: {cat_id}</p>")





def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Notes by category</h1><p>slug: {cat_slug}</p>")





def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return redirect(uri)

    return HttpResponse(f"<h1>Archive by years</h1><p>{year}</p>")




def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not Found</h1>")
