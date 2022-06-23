from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='home'),
    path('about/', About, name='about'),
    path('techniques/', TechniqueList, name='techniqueslist'),
    path('techniques/<int:id>', Technique, name='techniques')
    
    
]
