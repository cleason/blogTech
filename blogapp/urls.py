from django.urls import path
from . import views
from .views import BlogPostDetailView

app_name = "blogapp"

urlpatterns = [
    path('', views.index, name="index"),
    path('detail/<slug:slug>/', BlogPostDetailView.as_view(), name='detail'),
]