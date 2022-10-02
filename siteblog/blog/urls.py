from django.urls import path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', ListPosts.as_view(), name='category'),
    path('tag/<str:slug>/', get_tag, name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
]