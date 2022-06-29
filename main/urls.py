from django.urls import path
from .views import *
from main.custom_setting import *

urlpatterns = [
    path('', Index, name = 'home'),
    path('about/', About, name= URL_NAME_ABOUT),
    
    path( URL_PATH_ECT + '/<str:str>/<slug:slug>/', ShowECT, name = URL_NAME_ECT),
    path( URL_PATH_ECT + '/<slug:slug>/', ECTList, name = URL_NAME_ECT_LIST), #slug is cathegory of ect (for example game-console or mainframe)
    path( URL_PATH_ECT + '/add/', ECTAdd, name = URL_NAME_ADD ),
    
    path( URL_PATH_ARCHITECTURE + 's/', ListModel, name = URL_NAME_ARCHITECTURE_LIST),
    path( URL_PATH_ARCHITECTURE + '/<slug:slug>/', AboutModel, name = URL_NAME_ARCHITECTURE),
    
    path( URL_PATH_PROCESSOR + 's/', ListModel, name = URL_NAME_PROCESSOR_LIST),
    path( URL_PATH_PROCESSOR + '/<slug:slug>/', AboutModel, name = URL_NAME_PROCESSOR),
    
    path( URL_PATH_CATHEGORY + 's/', ListModel, name = URL_NAME_CATHEGORY_LIST),
    path( URL_PATH_CATHEGORY + '/<slug:slug>/', AboutModel, name = URL_NAME_CATHEGORY)
]
