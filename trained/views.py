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
from django.db import models
from django.core.management import call_command
from django.apps import apps
from .dynamic_models import *
from trained.dynamic_models import create_dynamic_model
from django.db import connection
from django.http import HttpResponse
from .models import *
# from .dynamic_models import create_dynamic_model
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
# from .forms import *

def menu(request):
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form.save() 
    else:
        form = NewCommentForm()

    return render(request, 'trained/train1.html', {'form': form})


from django.shortcuts import render
from .forms import *
from .models import *

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
        # return redirect('/trained/')
     
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

# def train_chat(request):   
#     return render(request, 'trained/chatbot-trainer.html')
from django.shortcuts import render
from .forms import *

def upload_picture(request):
    if request.method == 'POST':
        form = PictureUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = PictureUploadForm()
    
    my_model = Admin_panel.objects.first()
    return render(request, 'trained/index2.html', {'form': form})

from django.db import models

  # Define the DynamicModel at the module level

def user_register(request):
        if request.method == 'POST':
            input_types = {}
            column_names = []

            for field_name, field_value in request.POST.items():
                if field_name.endswith('_input_type'):
                    x = field_name.split('_')
                    field_name = x[0]  # Remove '_input_type' suffix

                    input_type = field_value
                    input_types[field_name] = input_type
                    column_names.append(field_name)
                    input_type = field_value
                    input_types[field_name] = input_type
                    my_object = user_panel.objects.create(input_label=field_name, input_type=input_type, parent_id=1)

            # Generate the CREATE TABLE SQL statement
            table_name = MyModel._meta.db_table
            columns = ', '.join([f"{column} VARCHAR(255)" for column in column_names])  # Modify the VARCHAR(255) to match your field types
            sql = f"CREATE TABLE {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, {columns})"

            # Execute the SQL statement
            with connection.cursor() as cursor:
                cursor.execute(sql)

        return render(request, 'trained/user_register.html')

def show_query(request):
    my_view = user_panel.objects.filter(parent_id=1).order_by('-id')
    my_view = my_view.reverse()
    if request.method == 'POST':
        # Retrieve form data
        table_name = MyModel._meta.db_table
        form_data = {}
        with connection.cursor() as cursor:
            cursor.execute(f"DESCRIBE {table_name}")
            columns = [column[0] for column in cursor.fetchall()]
        for column in columns:
            value = request.POST.get(column, '')
            print(value)
            form_data[column] = value

        # Save form data to the dynamically created table
        with connection.cursor() as cursor:
            columns = ', '.join(form_data.keys())
            values = ', '.join([f"'{value}'" for value in form_data.values()])
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
            cursor.execute(sql)
        
    return render(request, 'trained/show_query.html', {'my_view': my_view})

