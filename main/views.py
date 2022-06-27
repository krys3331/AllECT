from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from main.models import *

# Create your views here.

menu = [
    {'title':'Про сайт', 'url_page':'about'},
    {'title':'Додати техніку', 'url_page':'ectadd'},
    ]


def Index(request):
    about = '''
    ГОЛОВНА СТОРІНКА
    '''
    
    return render(request, 'main/main.html', {'cathegorys' : Cathegory.objects.all(), 'menu':menu, 'about':about})


def About(request):
    
    about = '''
    Сайт показує деякі технології в світі IT (ЕОМ, процессори, архітектури....)
    Сайт зроблений за допомогою fraemwork Django
    Source code - https://github.com/krys3331/AllECT
    '''
    return render(request, 'main/about.html', {'cathegorys' : Cathegory.objects.all(), 'menu':menu, 'about':about})

def ECT(request, slug):
    return get_object_or_404(ECT)

def ECTList(request):
    return HttpResponse("LIST")

def ECTAdd(request):
    return HttpResponse("ADD")

def PageNotFound(request, exception):
    return HttpResponseNotFound("PAGE NOT FOUND")