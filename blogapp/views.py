from django.utils import timezone
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import BlogPost

# Create your views here.

def index(request):
    posts = BlogPost.objects.all()
    return render(request, 'index.html', {'posts': posts})

class BlogPostDetailView(DetailView):
    model = BlogPost
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context


