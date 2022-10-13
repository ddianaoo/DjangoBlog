from django import template
from blog.models import *
from django.db.models import *


register = template.Library()


@register.inclusion_tag('blog/popular_posts.html')
def get_popular(cnt=3):
    posts = Post.objects.order_by("-views")[:cnt]
    return {"posts": posts}
