from django import forms

from .models import BlogPost


class BlogPostCreateFrom(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            "title",
            "sub_title",
            "content",
            "author"
        )


