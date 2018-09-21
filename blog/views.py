from django.shortcuts import render, get_object_or_404

# from .mocks import Post
from .models import Post


def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})


def show(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/show.html', {'post': post})