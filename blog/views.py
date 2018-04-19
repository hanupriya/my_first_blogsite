from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import Postform
from django.shortcuts import redirect
from django.utils import timezone
# Create your views here.


def post_list(request):
    posts = Post.objects.all() #filter(title__contains='Energy').order_by('published_date') #created a QuerySet
    return render(request, 'blog/post_list.html',{'posts':posts}) #request: anything from user / blog/post_list.html: template page /posts : to fill in the template with data

def post_detail(request,pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
       form = Postform()
    return render(request, 'blog/post_edit.html',{'form':form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
         form = Postform(request.POST, instance=post)
         if(form.is_valid()):
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
