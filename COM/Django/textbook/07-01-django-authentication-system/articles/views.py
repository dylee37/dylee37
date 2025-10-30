from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm


# Create your views here.
def index(request):
    """전체 게시글 목록을 조회하여 index.html 페이지를 렌더링"""
    # 1. Article 모델을 통해 DB에 저장된 모든 데이터를 조회
    articles = Article.objects.all()

    # 2. 조회된 데이터를 템플릿에 전달하기 위해 context 딕셔너리에 담음
    #    템플릿에서는 'articles'라는 키로 QuerySet 객체에 접근할 수 있음
    context = {
        'articles': articles,
    }
    # 3. request, 템플릿 경로, context를 render 함수에 전달하여 최종 HTML을 생성하고 사용자에게 응답
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    """특정 pk(Primary Key)를 가진 게시글 하나를 조회하여 detail.html 페이지를 렌더링"""
    # 1. URL로부터 전달받은 pk 값을 사용하여, 해당 pk를 가진 Article 객체 하나를 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 단일 게시글 객체를 context에 담아 템플릿에 전달
    context = {
        'article': article,
    }
    # 3. detail.html 템플릿을 렌더링
    return render(request, 'articles/detail.html', context)


def create(request):
    """
    GET 요청 시에는 게시글 생성 form 페이지를 렌더링하고,
    POST 요청 시에는 제출된 데이터를 DB에 저장 (new + create 역할 통합).
    """
    # --- POST 요청 처리 ---
    # 사용자가 form을 작성하고 '제출' 버튼을 눌렀을 때
    if request.method == 'POST':
        # form 인스턴스를 생성하고, 요청으로 들어온 데이터(request.POST)를 채움
        form = ArticleForm(request.POST)
        # 유효성 검사를 통과했다면
        if form.is_valid():
            # form 데이터를 DB에 저장하고, 저장된 Article 객체를 반환받음
            article = form.save()
            # 생성된 게시글의 상세 페이지로 리다이렉트
            return redirect('articles:detail', article.pk)
    # --- GET 요청 처리 ---
    # 사용자가 '/create/' URL에 처음 접속했을 때
    else:
        # 비어있는 form 인스턴스를 생성
        form = ArticleForm()
    # GET, POST 모든 경우에 context를 생성
    # POST 요청에서 유효성 검사를 실패한 경우, 오류 메시지가 담긴 form이 전달됨
    context = {
        'form': form,
    }
    # create.html 템플릿을 렌더링
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    """특정 pk를 가진 게시글을 DB에서 삭제"""
    # 1. 삭제할 게시글을 pk를 이용해 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회된 객체의 .delete() 메서드를 호출하여, DB에서 해당 레코드를 삭제(DELETE)
    article.delete()

    # 3. 게시글 삭제 후, 전체 목록 페이지로 이동
    return redirect('articles:index')


def update(request, pk):
    """
    GET 요청 시에는 기존 데이터를 담은 수정 form 페이지를 렌더링하고,
    POST 요청 시에는 제출된 데이터로 DB를 수정 (edit + update 역할 통합).
    """
    # 수정할 게시글을 DB에서 조회
    article = Article.objects.get(pk=pk)

    # --- POST 요청 처리 ---
    # 사용자가 수정 form을 '제출'했을 때
    if request.method == 'POST':
        # form 인스턴스를 생성하되,
        # 1. request.POST: 사용자가 제출한 새로운 데이터로 채우고,
        # 2. instance=article: 이 데이터가 어떤 기존 객체를 수정할 것인지 지정
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # 유효성 검사를 통과하면 DB에 변경사항을 저장
            form.save()
            # 수정된 게시글의 상세 페이지로 리다이렉트
            return redirect('articles:detail', article.pk)

    # --- GET 요청 처리 ---
    # 사용자가 '/update/' URL에 처음 접속했을 때
    else:
        # form 인스턴스를 생성하되,
        # instance=article: DB에서 조회한 기존 데이터(article)로 form을 미리 채움
        form = ArticleForm(instance=article)

    # GET, POST 모든 경우에 context를 생성
    context = {
        # update.html에서 '{{ article.pk }}'와 같이 사용하기 위해 전달
        'article': article,
        # GET: 기존 데이터가 채워진 form
        # POST (유효성 실패 시): 오류 메시지와 사용자가 입력했던 데이터가 채워진 form
        'form': form,
    }
    # update.html 템플릿을 렌더링
    return render(request, 'articles/update.html', context)
