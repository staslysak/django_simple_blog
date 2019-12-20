from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tag, Post
from .utils import *
from .forms import TagForm, PostForm

# Create your views here.
class TagDetails(ObjectDetailMixin, View):
  model = Tag
  template = 'blog/tag_details.html'


class TagList(ObjectListMixin, View):
  model = Tag
  template = 'blog/tags_list.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
  form_model = TagForm
  template = 'blog/tag_create.html'
  raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
  model = Tag
  form_model = TagForm
  template = 'blog/tag_update_form.html'
  raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
  model = Tag
  template = 'blog/tag_delete_form.html'
  redirect_url = 'tags_list_url'    
  raise_exception = True
 
 
class PostDetails(ObjectDetailMixin, View):
  model = Post
  template = 'blog/post_details.html'


class PostList(ObjectListMixin, View):
  model = Post
  template = 'blog/index.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
  form_model = PostForm
  template = 'blog/post_create.html'
  raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
  model = Post
  form_model = PostForm
  template = 'blog/post_update_form.html'
  raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
  model = Post
  template = 'blog/post_delete_form.html'
  redirect_url = 'posts_list_url'    
  raise_exception = True
