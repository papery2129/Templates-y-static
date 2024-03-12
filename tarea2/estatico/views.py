from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def http_response_view(request):
    return HttpResponse('<ul> <li>Videojuegos</li> <li>Manga</li> <li>star wars</li></ul') 

def index(request):
    text = {'lista': "videojuegos, star wars, musica"}
    return render(request, 'tarea2/index.html', context=text)
    #return HttpResponse("<h1>")
