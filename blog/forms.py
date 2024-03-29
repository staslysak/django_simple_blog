from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
  class Meta():
    model = Tag
    fields = ['title', 'slug']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
      'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
    }


  def clean_slug(self):
    new_slug = self.cleaned_data['slug'].lower()

    if new_slug == 'create':
      raise ValidationError('Slug may not be "Create"')

    if Tag.objects.filter(slug__iexact=new_slug).count():
      raise ValidationError('Slug "{}" is already created'.format(new_slug))

    return new_slug


class PostForm(forms.ModelForm):
  class Meta():
    model = Post
    fields = ['title', 'slug', 'body', 'tags']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
      'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
      'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Body'}),
      'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
    }


  def clean_slug(self):
    new_slug = self.cleaned_data['slug'].lower()

    if new_slug == 'create':
      raise ValidationError('Slug may not be "Create"')

    # if Tag.objects.filter(slug__iexact=new_slug).count():
    #   raise ValidationError('Slug "{}" is already created'.format(new_slug))

    return new_slug
