from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

# 전체 게시글 조회(1) 후 메인 페이지 응답(2)
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# 게시글 상세 페이지를 응답하는 함수
# 1. 몇 번 게시글인지를 DB에 조회
# 2. 조회한 상세 게시글 데이터를 템플릿과 함께 응답
def detail(request, pk):
    # pk는 urls.py의 변수명과 동일
    # 1. 단일 게시글 조회
    # queryset API method ==> get()

    article = Article.objects.get(pk=pk)  # 오른쪽의 pk는 detail 함수의 매개변수
    
    # Article.objects.get(id = pk)

    # 2. 단일 게시글 데이터와 템플릿을 응답
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 1. 사용자로부터 입력 받은 데이터를 추출
# 2. 추출한 데이터를 DB에 저장
# 3. 저장이 완료되었다는 페이지를 응답

def create(request):
    # 1.
    title = request.POST.get('title')
    content = request.POST.get('content')


    # 2. DB 저장
    # 2.1 
    """
    article = Article()
    article.title = title  # 오른쪽 title은 위에서 추출한 변수
    article.content = content
    article.save() 
"""
    # 2.2
    article = Article(title=title, content=content)  # 저장 전에 유형 검사
    article.save()

    # 2.3
    #Article.objects.create(title=title, content=content)
    #return render(request, 'articles/create.html')
    # 클라이언트한테 새로운 주소로 요청을 보내게끔 시켜야 함
    return redirect('articles:index', article)

