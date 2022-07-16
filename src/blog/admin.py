from django.contrib import admin

# Register your models here.
from blog.models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    #les champs affichés
    list_display = ("title", "slug", "published", "date", "author", "word_count")
    #les champs éditables directement dans l'affichage
    list_editable = ("published",)
    #La barre de recherche et les champs recherchables
    search_fields = ('title', 'slug')
    #les champs qui ont des filtres
    #list_filter = ('published', 'author',)
    #les champs deroulant avec barre de recherche
    autocomplete_fields = ('author',)
    #les champs many to many
    filter_horizontal = ('category',)
    #limiter le nombre d'article par page
    list_per_page = 10
