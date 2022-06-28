from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('about/', About, name='about'),
    path('ECTs/', ECTList, name='ectlist'),
    path('ECTs/<slug:slug>', ECT, name='ect'),
    path('ECTs/add', ECTAdd, name='ectadd' ),
    path('Archs/', ArchList, name='archlist'),
    path('Archs/<slug:slug>', Arch, name='arch'),
    path('Processors/', ProcessorList, name='processlist'),
    path('Processors/<slug:slug>', Processor, name='process')
]
