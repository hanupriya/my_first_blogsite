from django.shortcuts import render
from .models import Post
from django.utils import timezone
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(title__contains='Energy').order_by('published_date') #created a QuerySet
    return render(request, 'blog/post_list.html',{'posts':posts}) #request: anything from user / blog/post_list.html: template page /posts : to fill in the template with data
