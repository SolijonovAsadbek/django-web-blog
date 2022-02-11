from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
from blog.models import Post

object_list = ""


def search(request):
    global object_list, articles
    req = request.GET.get('title', '')
    print(req)
    if req and req != "":
        object_list = Post.objects.filter(title__contains=req).all()
        articles = len(object_list)
    else:
        articles = 0

    return render(request, 'base.html',
                  {'title': req, 'object_list': object_list, "articles": articles})


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    articles = Post.objects.count()


class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'


class PostCreate(CreateView):
    model = Post
    template_name = 'newpost.html'
    fields = ['title', 'body', 'author']
