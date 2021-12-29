from django.http import request
from django.shortcuts import get_object_or_404, render
from django.urls.conf import path
from . models import Blog
# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    return render(request, 'allblogs.html', {'blogs': blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'d_blog': detailblog})
