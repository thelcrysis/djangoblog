from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def all_posts(request):
    posts = Post.objects.all().order_by('date')
    return render(request, "posts/allposts.html", {'posts': posts})
