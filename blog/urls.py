from django.urls import path

from blog.views import BlogListView, PostDetail, search, PostCreate

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='postdetail'),
    path('search/', search, name='search'),
    path('post/new', PostCreate.as_view(), name='newpost'),
]
