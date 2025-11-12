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
    # print(request.POST)
    title = request.POST['title']
    content = request.POST.get('content')

    # 레코드 생성을 위해 Article 인스턴스를 생성
    article = Article(title=title, content=content)    

    # DB에 실제 레코드 생성
    article.save()

    # ret = redirect(f'/articles/{article.pk}/')
    # return ret 
    return redirect('articles:detail', article.pk)
    
def delete(request, pk):
    if request.method == 'POST':        

        article = Article.objects.get(pk=pk)
        article.delete()

    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)

    title = request.POST['title']
    content = request.POST.get('content')

    article.title = title
    article.content = content

    article.save()

    return redirect('articles:detail', article.pk) 