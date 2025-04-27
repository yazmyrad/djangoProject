from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from .models import Blog
from .forms import BlogForm
from taggit.models import Tag
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request, tag_slug=None):
    blogs = Blog.objects.all()
    user  = request.user
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        blogs = blogs.filter(tags__in=[tag])
        
    return render(request, "study/card.html", {'blogs':blogs, 'user':user})

@login_required(login_url="/login/")
def blog(request, slug):
    blog  = Blog.objects.get(slug=slug)
    user  = request.user
    return render(request, "study/blog_template.html", {'blog': blog, 'user':user})

@login_required(login_url="/login/")
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.create(
                title  = form.cleaned_data['title'],
                content= form.cleaned_data['content'],
                author = request.user,
                source = form.cleaned_data['source']
            )
            print(f"user {request.user}")
            tags = [tag.strip() for tag in form.cleaned_data['tags'].split(' ')]
            blog.tags.set(tags)
            
        return redirect("/home")
    else:
        form = BlogForm()
        user =  request.user
    return render(request, "study/create_blog.html", {'form':form, 'user':user}) 

def pageNotFound(request, exeptaion):
    return HttpResponseNotFound("Sorry for this")