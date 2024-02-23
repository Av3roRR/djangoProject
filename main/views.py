from django.http import HttpResponse
from django.shortcuts import render
from django.template import context

# Create your views here.
def index(request):
    context = {
        'title': 'Home - Главная    ',
        'content': "Магазин мебели HOME"
    }
    
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - Главная    ',
        'content': "Магазин мебели HOME",
        'text_on_page': "Мы крутая компания"
    }
    
    return render(request, 'main/about.html', context)

