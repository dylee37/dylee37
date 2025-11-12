from django.urls import path
from . import views

urlpatterns = [
    # 전체글 조회(GET) 및 새 게시글 작성(POS)
    path('articles/', views.article_list),

    # 글 상세 조회(GET), 수정(PUT), 삭제(DELETE)
    path('articles/<int:article_pk>/', views.article_detail),
]
