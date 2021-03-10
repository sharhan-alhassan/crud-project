from django.shortcuts import render

from .models import Core
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(ListView):
    model = Core
    template_name = 'core/index.html'
    context_object_name = 'index'

class SingleView(DetailView):
    model = Core
    template_name = 'core/single.html'
    context_object_name = 'post'

class PostsView(ListView):
    model = Core
    template_name = 'core/posts.html'
    context_object_name = 'post_list'

class AddView(CreateView):
    '''Basically a form. Someone types in and add new post'''
    model = Core
    template_name = 'core/add.html'
    fields = '__all__' #take all the fields from the db and put that into a form
    success_url = reverse_lazy('core:posts')