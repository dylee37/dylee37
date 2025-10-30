from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    # 지금 이 시점에 article.pk =? None

    article.save()
    # 여기서는 article.pk => 유효한 값
    # 게시글의 상세 페이지를 클라이언트에게 보여준다
    # 클라이언트에게 상세 페이지에 대한 요청을 다시 하라는 응답을 보냄
    return redirect(f'/articles/{article.pk}/')


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    pass

def update(request, pk):
    pass

