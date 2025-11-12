# articles/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 전체 게시글 조회(GET) / 게시글 생성(POST): /api/v1/articles/
    path('articles/', views.article_list),
    # 게시글 상세 조회(GET) / 삭제(DELETE) / 수정(PUT, PATCH): /api/v1/articles/<int:article_pk>/
    path('articles/<int:articles_pk>/', views.article_detail),
]