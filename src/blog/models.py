from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=36)
    slug = models.SlugField(blank=True)


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    date = models.DateField(blank=True, null=True)
    content = models.TextField()
    description = models.TextField()

    @property
    def publish_string(self):
        if self.published:
            return "L'article est publié"
        return "L'article est inaccessible"

    def save(self, *args,  **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return self.title

    @property
    def number_of_words(self):
        return len(self.content.split())

    def get_absolute_path(self):
        return reverse("blog-post", kwargs={"slug": self.slug})
