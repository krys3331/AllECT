from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from main.models import *

# Create your views here.

menu = [
    {'title':'Про сайт', 'url_page':'about'},
    {'title':'Додати техніку', 'url_page':'ectadd'},
    ]


def Index(request):
    return render(request, 'main/main.html', {'menu':menu})


def About(request):
    
    about = '''
    Сайт показує деякі технології в світі IT (ЕОМ, процессори, архітектури....)
    Сайт зроблений за допомогою Framework Django
    Source code - https://github.com/krys3331/AllECT
    '''
    return render(request, 'main/about.html', {'menu':menu, 'about':about})

def ECT(request, slug):
    return get_object_or_404(ECT)

def ECTList(request):
    return HttpResponse("LIST")

def ECTAdd(request):
    return HttpResponse("ADD")


def ArchList(request):
    
    arch = Architecture.objects.all()
    
    return render(request,'main/archlist.html', {'menu':menu, 'archl':arch, })

def Arch(request, slug):
    arch = get_object_or_404(Architecture, slug=slug)
    return render(request,'main/arch.html', {'menu':menu, 'arch':arch})

def ProcessorList(request):
    return HttpResponse("PROC LIST")

def Processor(request, slug):
    return HttpResponse(f"Proc:{slug}")

def PageNotFound(request, exception):
    # return render(request, 'main/notfound.html')
    return HttpResponseNotFound("PAGE NOT FOUND")