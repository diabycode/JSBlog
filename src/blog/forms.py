from django import forms

from .models import BlogPost


class BlogPostCreateForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            "title",
            "sub_title",
            "content",
            "author",

        )
        widget = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Hello",
                }
            ),

        }


class MyDateInput(forms.DateInput):
    input_type = "date"


class BlogPostEditForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            "title",
            "sub_title",
            "content",
            "published",
            "author",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "placeholder": "Entrer un titre pour l'article",
                }
            ),
            "publish_date": MyDateInput(),
        }

