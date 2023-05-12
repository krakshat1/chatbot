from django import forms
from .models import *

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menuss
        fields = ('name', 'answer')

from django import forms

from mptt.forms import TreeNodeChoiceField


class NewCommentForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Menuss.objects.all())
    class Meta:
        model = Menuss
        fields = ('name', 'parent', 'answer')

       
from django import forms
from .models import Node

class NodeForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=Node.objects.all())

    class Meta:
        model = Node
        fields = ['name', 'parent','answer']
