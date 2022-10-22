from django.views.generic import ListView, DetailView
from .models import *
from django.core.paginator import Paginator
from django.db.models import F



class PostsByTag(ListView):
    context_object_name = 'posts'
    paginate_by = 4
    model = Tag
    template_name = 'blog/tag.html'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


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


class GetPost(DetailView):
    model = Post
    context_object_name = 'post'
    # pk_url_kwarg = 'post_slug'
    template_name = 'blog/single_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context