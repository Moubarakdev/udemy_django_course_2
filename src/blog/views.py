import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import BlogPost
from django.contrib.auth.decorators import login_required, user_passes_test
from website.forms import SignupForm
from blog.forms import BlogPostForm


# Create your views here.)

#vue basée sur les classes

class BlogIndexView(ListView):
    #on met le model ou soit on passe par une requête avec queryset
    model = BlogPost
    #queryset = BlogPost.objects.filter(published=True)
    template_name = "blog/index.html"
    #le context_object_name nous permets de spécifier le nom de la données à manipuler dans le template
    context_object_name = "posts"


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/post.html"
    context_object_name = "post"


class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = "blog/post_form.html"
    form_class = BlogPostForm
    context_object_name = "form"
    success_url = reverse_lazy("blog-index")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        form.instance.published = True
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["submit_text"] = "Créer"
        return context


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = "blog/post_form.html"
    form_class = BlogPostForm
    #on peut rediriger avec cette fonction ou avec l'attribut "success_url
    def get_success_url(self):
        return reverse("blog-index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["submit_text"] = "Modifier"
        return context

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog\delete_post.html"
    context_object_name = 'post'
    success_url = reverse_lazy("blog-index")


#vues basées sur les fonctions


def blog_posts(request):
    posts = BlogPost.objects.all()
    return render(request, "blog/index.html", context={"posts": posts})


def blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, 'blog/post.html', context={"post": post})


def blog_post_create(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.instance.published = True
            if request.user.is_authenticated:
                form.instance.author = request.user
            form.save()
        return HttpResponseRedirect(reverse("blog-index"))
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
