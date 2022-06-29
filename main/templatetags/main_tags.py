from atexit import register
from django import template
from main.models import *

register = template.Library()

@register.simple_tag()
def get_processors():
    return Proccessor.objects.all()

@register.simple_tag()
def get_architectures():
    return Architecture.objects.all()

@register.simple_tag()
def get_cathegorys():
    return Cathegory.objects.all()

@register.simple_tag()
def get_ect():
    pass
