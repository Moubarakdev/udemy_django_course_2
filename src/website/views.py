from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"
    title = "default"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = self.title
        return context


def home(request):
    return render(request, 'index.html', {"title": "Acceuil du site"})