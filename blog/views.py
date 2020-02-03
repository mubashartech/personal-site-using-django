from django.shortcuts import render
from .models import Post
# Create your views here.

def blog_Home(request):
    p = Post.objects.all()
    context = {'posts': p}
    return render(request, 'blog/home.html', context)
def blog_Detail(request, id):
    p = Post.objects.get(id=id)
    context = {'post': p}
    return render(request, 'blog/detail.html', context)
