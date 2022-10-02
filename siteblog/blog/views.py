from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator



def get_post(request, slug):
    return HttpResponse('hello')
    #need to change this function


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CLASSIC BLOG DESIGN'.title()
        return context


class ListPosts(ListView):
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/category.html'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

