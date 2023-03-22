from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def index(request, *args, **kwargs):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

def detail(request):
    posts = BlogPost.objects.all()
    return render(request, 'detail.html', {'posts': posts})
