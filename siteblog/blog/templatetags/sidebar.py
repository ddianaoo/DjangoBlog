from django import template
from blog.models import *
from django.db.models import *


register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by("-views")[:cnt]
    return {"posts": posts}


@register.inclusion_tag('blog/list_of_tags.html')
def get_tags():
    tags = Tag.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {"tags": tags}