from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return render(request, template_name='index.html')


class KnihyListView(ListView):
    model = kniha
    context_object_name = 'kniha_list'
    template_name = 'list.html'


class KnihyDetailView(DetailView):
    model = kniha
    context_object_name = 'kniha'
    template_name = 'detail.html'


class KnihyHomeView(ListView):
    model = kniha
    context_object_name = 'kniha_index'
    template_name = 'index.html'
