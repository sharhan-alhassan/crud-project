from django.shortcuts import render

from .models import Core
from django.views.generic import ListView, DetailView

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
    template_name = 'core/admin.html'
    context_object_name = 'post_list'