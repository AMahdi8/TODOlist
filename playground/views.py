from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def hello(request):
    return HttpResponse('hello')


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})
