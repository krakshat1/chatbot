from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    #path('admin/', views.index,name = 'index'),
    path('train/', views.menu,name='menu'),
    path('trained/', views.train_chat,name='train_chat'),
    path('train2/', views.create_node,name='node'),
    path('edit_menu/<str:pk>/', views.edit_menu, name='edit_menu'),
    path('delete_menu/<str:pk>/', views.delete_menu, name='delete_menu'),
    path('my_view/<str:pk>/', views.my_view, name='my_view'),
    path('add_submenu/<str:pk>/', views.add_submenu, name='add_submenu'),
    path('showing/', views.train_chat, name='train_chat')


    
    ]

