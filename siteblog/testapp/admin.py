from django.contrib import admin
from .models import *
# from mptt.admin import MPTTModelAdmin
from mptt.admin import DraggableMPTTAdmin


# class CustomMPTTModelAdmin(MPTTModelAdmin):
#     mptt_level_indent = 20

# admin.site.register(Rubric, CustomMPTTModelAdmin)

admin.site.register(
    Rubric,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)

admin.site.register(Article)
