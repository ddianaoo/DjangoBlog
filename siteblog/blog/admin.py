from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget



class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'content', 'category', 'photo', 'created_at', 'views']
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']
    readonly_fields = ['views']
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
