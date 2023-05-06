from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import *

def menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = MenuForm()

    return render(request, 'trained/train1.html', {'form': form})
