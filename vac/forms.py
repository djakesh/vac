from django import forms

from vac.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'description', 'image')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'description', 'image')

