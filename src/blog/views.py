from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.)
def blog_posts(request):
    blog_post = get_object_or_404(BlogPost, pk=4)
    return render(request, "blog/post.html", context={"blog_post": blog_post})