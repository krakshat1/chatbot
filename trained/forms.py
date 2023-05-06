from django import forms
from .models import *

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ('question1', 'answer1')



class SubmenuForm(forms.ModelForm):
    class Meta:
        model = Submenu
        fields = ('name', 'menu', 'answer1')