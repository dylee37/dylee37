from django.shortcuts import render, redirect
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    pass


def create(request):
    pass


def delete(request, pk):
    pass

def update(request, pk):
    pass