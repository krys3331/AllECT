from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from main.models import *

# Create your views here.


def Index(request):
    
    return render(request, 'main/index.html', {'cathegorys' : Cathegory.objects.all()})


def About(request):
    return render(request, 'main/about.html', {'cathegorys' : Cathegory.objects.all()})

def Technique(request, id):
    return HttpResponse(f"GGGGG:{id}")

def TechniqueList(request):
    return HttpResponse("ABOUT")

def PageNotFound(request, exception):
    return HttpResponseNotFound("PAGE NOT FOUND")