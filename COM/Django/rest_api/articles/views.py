from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

# 1. 데코레이터 필요
@api_view(['GET', 'POST', ])  # 허용할 메소드의 문자열 리스트
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)

        # 2. Response 객체를 반환해야 한다.
        return Response(serializer.data)

    elif request.method =='POST':
        # 클라이언트가 전송한 데이터는 request.data
        # request.data의 유효성 검증이 필요
        serializer = ArticleSerializer(data=request.daeta)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

        # return Response(serializer.errors, status=400)



@api_view(['GET',])
def article_detail(request, article_pk):
    if request.method == 'GET':
        article = Article.objects.get(pk=article_pk)
        serializer = ArticleSerializer(article)

        return Response(serializer.data)
