from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 게시글 조회: GET  articles/
    path('', views.index, name='index'),

    # 상세 게시글 조회: GET  articles/1/
    path('<int:pk>/', views.detail, name='detail'),
    
    # 게시글 생성
    # 1. 게시글 작성 폼 요청: GET articles/new/
    # 2. 게시글 DB 저장 요청: POST articles/create/
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),

    # 게시글 삭제: POST  articles/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 게시글 수정
    # 1. 게시글 수정 폼 요청:GET  articles/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),
    # 2. 수정된 내용 DB 저장: POST  articles/1/update/
    path('<int:pk>/update/', views.update, name='update'),
]
