from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [    
    # 전체 게시글 조회 /articles/
    path('', views.index, name='index'),

    # 게시글 상세 조회 /articles/1/
    path('<int:pk>/', views.detail, name='detail'),

    # 새글 작성 /articles/create/
    # GET: 양식 요청, POST: 테이블에 저장
    path('create/', views.create, name='create'),

    # 삭제하기 /articles/1/delete/
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 수정하기 /articles/1/update/
    path('<int:pk>/update/', views.update, name='update'),

]
