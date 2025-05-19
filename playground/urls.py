from django.urls import path
from .views import hello, all_posts

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('all_posts/', all_posts, name='all-posts'),
]
