from django import forms
from bbs.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('content', )