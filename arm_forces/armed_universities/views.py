from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Armed_university



def index(request):
    data = {}
    return render(request, 'armed_universities/index.html', context=data)


def about(request):
    context = {'title': 'О сайте'}

    return render(request, 'armed_universities/about.html', context=context)


def all_schools(request):
    posts = Armed_university.objects.all()
    context = {'title': 'Все вузы', 'posts': posts}

    return render(request, 'armed_universities/all_schools.html', context=context)


def certain(request, name):
    post = Armed_university.objects.get(slug=name)
    context = {'title': name, 'post': post}

    return render(request, 'armed_universities/certain.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

