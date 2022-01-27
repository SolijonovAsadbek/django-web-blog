from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'
