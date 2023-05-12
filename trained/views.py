from django.shortcuts import render,get_object_or_404

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
        menu = request.POST.get('menu')
        my_model_instance = Node(name=menu)
        my_model_instance.save()
        print(menu)

    data  = Node.objects.all()
    context = {'data': data}
        
    return render(request, 'trained/train.html',context)