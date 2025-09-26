from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int: 변수명>')
    path('<int:pk>/', views.detail, name='detail'),
    # pk = id (primary key)
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
