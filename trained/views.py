from django.shortcuts import render,get_object_or_404
import re
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, HttpResponse,redirect
import random
import json
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from .models import *
import logging

# def activity_logging(activity):
#     activity = activity
#     ip_address = request.META.get('REMOTE_ADDR')
#         if ip_address:
#             response = requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey=YOUR_API_KEY&ip={ip_address}')
#             if response.status_code == 200:
#                 location_data = response.json()
#                 location_info = f"{location_data['city']}, {location_data['country_name']}"
#                 location = location_info
#     activity_log = ActivityLog(activity=activity, ip_address=ip_address)


# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)
# Create your views here.
from django.shortcuts import render,redirect
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
        data = Node.objects.all()
    else:
        form = NodeForm()
        data = Node.objects.all()

    nodes = Node.objects.all()
    context = {
        'form': form,
        'nodes': nodes,
        'data': data
    }
    return render(request, 'trained/train2.html', context)

def edit_menu(request, pk):
    book = get_object_or_404(Node, id=pk)
    form = NodeForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/trained/')
     
    return render(request, 'trained/edit_menu.html', {'form': form, 'book': book})

def delete_menu(request, pk):
    my_object = get_object_or_404(Node, id=pk)

    if request.method == 'POST':
        # Delete the object
        my_object.delete()
        return redirect('/trained/')
    return render(request, 'trained/train2.html')

def train_chat(request):

    if request.method == 'POST':
        menu = request.POST.get('menu').lower()
        my_model_instance = Node(name=menu)
        my_model_instance.save()
        #print(menu)

    data  = Node.objects.filter(parent__isnull=True)
    context = {'data': data}
        
    return render(request, 'trained/train.html',context)

def my_view(request,pk):
    parent = Node.objects.get(id=pk)
    queryset = Node.objects.filter(parent__isnull=False, parent=parent)
    data = []
    for model in queryset:
        data.append(model.name)
    return JsonResponse(data, safe=False)

def add_submenu(request,pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        answer = request.POST.get('answer')
        parent = Node.objects.get(id=pk)
        data = {
        'name': name,
        'answer': answer,
        'parent': parent,
        }
        my_object = Node.objects.create(**data)
    parent = Node.objects.get(id=pk)
    queryset = Node.objects.filter(parent__isnull=False, parent=parent)
    # data = []
    # for model in queryset:
    #     data.append(model.name)
    return render(request, 'trained/show.html',{'data': queryset})

def train_chat(request):   
    return render(request, 'trained/chatbot-trainer.html')