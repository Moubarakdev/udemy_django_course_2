from django import forms
from blog.models import BlogPost
JOBS = (
    ("python", "developpeur python"),
    ("javascript", "developpeur javaScript"),
    ("csharp", "Développeur C#"),
)


class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if '$' in pseudo:
            raise forms.ValidationError("Le pseudo ne peut pas contenir de $")
        return pseudo


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields ="__all__"
        labels = {"title": "Titre",
                  "category": "Catégorie",
                  "author": "Auteur"}
        widgets = {"date": forms.SelectDateWidget(years=range(1990, 2040)),
                   "title": forms.TextInput(attrs={"placeholder": "titre"})}

