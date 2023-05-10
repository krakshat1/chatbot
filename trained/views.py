from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import *

def menu(request):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = NewCommentForm()

    return render(request, 'trained/train1.html', {'form': form})


from django.shortcuts import render
from .forms import NodeForm
from .models import Node

def create_node(request):
    if request.method == 'POST':
        form = NodeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NodeForm()

    nodes = Node.objects.all()
    context = {
        'form': form,
        'nodes': nodes,
    }
    return render(request, 'trained/train2.html', context)
