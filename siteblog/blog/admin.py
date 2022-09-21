from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


#model - Post
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'category', 'get_photo', 'created_at']
    list_display_links = ['id', 'title', 'slug']
    search_fields = ['title', 'slug']
    list_filter = ['category', 'author', 'tags']
    readonly_fields = ['views', 'get_photo',  'created_at']
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_on_top = True # when you make some changes you will can save it with buttons on the top of the page
    #save_as = True # in admin/ you can see the button "save as a new obj" when you add some changes
    fields = ['title', 'slug', 'author',
              'content', 'get_photo',
              'photo', 'category', 'tags',
              'created_at', 'views'] #fields, which you can see when you want to edit a post

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="85">')
            #return mark_safe('хуй')
        # else:
        #     return mark_safe(f'<img src="https://picsum.photos/id/1060/75/40/?blur=2">')
        return '-'

    get_photo.short_description = 'Миниатюра'



#model - Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}



#model - Tag
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)


admin.site.site_header = 'Админка для крутых пацанов'