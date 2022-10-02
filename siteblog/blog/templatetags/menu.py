from django import template
from blog.models import Category
from django.db.models import *



register = template.Library()


@register.inclusion_tag('blog/menu_cat.html')
def show_menu(menu_class='menu'):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('posts')).filter(cnt__gt=0)
    return {"categories": categories, "menu_class": menu_class}