from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post

def home(request):
    posts = Post.objects.all()[0:10:-1]
    return render(request, 'index.html', {"posts" : posts})

def about(request):
    return HttpResponse("about")


