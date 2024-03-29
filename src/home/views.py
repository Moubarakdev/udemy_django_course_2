from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import template


def index(request):
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render())


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        # if load_template == 'admin':
        #   return HttpResponseRedirect(reverse('admin:index'))
        # context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
