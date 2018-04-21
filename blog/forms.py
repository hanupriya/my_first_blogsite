from django import forms
from .models import Post
from .models import Comment

class Postform(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

class Commentform(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','text',)

