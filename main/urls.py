from django.urls import path
from .views import *
from main.custom_setting import *

urlpatterns = [
    path('', Index, name = 'home'),
    path(URL_ABOUT + '/', About, name= URL_ABOUT),
    
    path( URL_ECT + '/<str:str>/<slug:slug>/', ShowECT, name = URL_ECT),
    path( URL_ECT + '/<slug:slug>/', ECTList, name = URL_ECT), #slug is cathegory of ect (for example game-console or mainframe)
    
    path( URL_ADD + '/', AddChoose, name = URL_ADD ),
    path( URL_ADD + '/<slug:slug>', AddModel, name = URL_ADD ),
    
    path( URL_ARCHITECTURE + 's/', ListModel, name = URL_ARCHITECTURE),
    path( URL_ARCHITECTURE + '/<slug:slug>/', AboutModel, name = URL_ARCHITECTURE),
    
    path( URL_PROCESSOR + 's/', ListModel, name = URL_PROCESSOR),
    path( URL_PROCESSOR + '/<slug:slug>/', AboutModel, name = URL_PROCESSOR),
    
    path( URL_CATHEGORY + 's/', ListModel, name = URL_CATHEGORY),
    path( URL_CATHEGORY + '/<slug:slug>/', AboutModel, name = URL_CATHEGORY)
]
