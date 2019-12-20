from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.db.models import Q
# from django.http import HttpResponse
from .models import *


class ObjectDetailMixin:
  model = None
  template = None

  def get(self, request, slug):
    obj = get_object_or_404(self.model, slug__iexact=slug)
    return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_obj': obj})


class ObjectListMixin:
  model = None
  template = None

  def get(self, request):
    search_query = request.GET.get('search', '')

    if search_query and self.model.__name__.lower() == 'post':
      objs = self.model.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
      objs = self.model.objects.all()

    paginator = Paginator(objs, 2)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    # '{}s'.format(self.model.__name__.lower())
    is_paginated = page.has_other_pages()
    
    if page.has_previous():
      prev_url = '?page={}'.format(page.previous_page_number())
    else:
      prev_url = ''
    
    if page.has_next():
      next_url = '?page={}'.format(page.next_page_number())
    else:
      next_url = ''

    return render(request, self.template, context={
      'objs': page,
      'next_url': next_url,
      'prev_url': prev_url,
      'is_paginated': is_paginated,
      'search_query': search_query
    })


class ObjectCreateMixin:
  form_model = None
  template = None

  def get(self, request):
    form = self.form_model()
    return render(request, self.template, context={'form': form})

  def post(self, request):
    bound_form = self.form_model(request.POST)

    if bound_form.is_valid():
      new_obj = bound_form.save()
      return redirect(new_obj)

    return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
  model = None
  form_model = None
  template = None

  def get(self, request, slug):
    obj = self.model.objects.get(slug__iexact=slug)
    bound_form = self.form_model(instance=obj)
    return render(request, self.template, context={'form': bound_form, 'obj': obj})

  def post(self, request, slug):
    obj = self.model.objects.get(slug__iexact=slug)
    bound_form = self.form_model(request.POST, instance=obj)

    if bound_form.is_valid():
      new_obj = bound_form.save()
      return redirect(new_obj)

    return render(request, self.template, context={'form':bound_form, 'obj': obj})


class ObjectDeleteMixin:
  model = None
  template = None
  redirect_url = None

  def get(self, requset, slug):
    obj = self.model.objects.get(slug__iexact=slug)
    return render(requset, self.template, context={'obj': obj})

  def post(self, requset, slug):
    obj = self.model.objects.get(slug__iexact=slug)
    obj.delete()
    return redirect(reverse(self.redirect_url))
