from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Create your views here.
from blog.models import Post

object_list = ""


def search(request):
    global object_list
    req = request.GET.get('title', '')
    if req and req != "":
        object_list = Post.objects.filter(title__contains=req).all()

    return render(request, 'base.html', {'title': req, 'object_list': object_list})


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'postdetail.html'
