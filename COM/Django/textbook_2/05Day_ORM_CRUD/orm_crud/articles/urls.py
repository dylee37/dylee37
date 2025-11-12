from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # 전체 조회 articles/
    path('', views.index, name='index'),

    # 상세 조회 articles/10/
    path('<int:pk>/', views.detail, name='detail'),
    
    # 작성 폼요청 articles/new/
    path('new/', views.new, name='new'),

    # 레코드 생성 요청 articles/create/
    path('create/', views.create, name='create'),

    # 삭제 articles/1/delete/    
    path('<int:pk>/delete/', views.delete, name='delete'),

    # 수정이 폼 요청 articles/1/edit/
    path('<int:pk>/edit/', views.edit, name='edit'),

    # 실제 레코드 수정 요청 articles/1/update/
    path('<int:pk>/update/', views.update, name='update'),
]
