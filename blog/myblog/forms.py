from django import forms
from .models import Post, Category, Comment

categories = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','tags','author','category','body','summary')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=categories,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','tags','body','category','summary')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'tags':forms.TextInput(attrs={'class':'form-control'}),
            'category':forms.Select(choices=categories,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'summary':forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control','cols': 80, 'rows': 3}),

        }