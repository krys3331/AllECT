from enum import unique
from lib2to3.pytree import Base
from django import forms
from .models import *


class AddProcessorForm(forms.ModelForm):
    class Meta:
        model = Proccessor
        fields = '__all__'
        
class AddArchitectureForm(forms.ModelForm):
    class Meta:
        model = Architecture
        fields = '__all__'


class AddCathegoryForm(forms.ModelForm):
    class Meta:
        model = Cathegory
        fields = '__all__'


class AddECTForm(forms.ModelForm):
   class Meta:
        model = ECT
        fields = '__all__'