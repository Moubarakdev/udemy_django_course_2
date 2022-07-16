import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required, user_passes_test
from website.forms import SignupForm, BlogPostForm


# Create your views here.)
def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', context={"post": post})


def blog_form_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(request.path)
    else:
        form = BlogPostForm()
    return render(request, 'blog/post_form.html', context={"form": form})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Merci de vous être inscrit au site.")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", context={"form": form})
