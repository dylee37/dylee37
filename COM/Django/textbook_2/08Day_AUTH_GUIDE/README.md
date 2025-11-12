# Authentication

[TOC]

-----------------------

## 1. 사전 준비

- 기본 [CRUD 코드](authentication_template/)에서 진행하기

#### Accounts 앱 생성

```bash
$ python manage.py startapp accounts
```

- `accounts` 앱을 `settings.py`에 등록

```python
# settings.py

INSTALLED_APPS = [
    'articles',
    'accounts',            # <-----------------

    # . . .
]
```

#### `accounts/` 로 시작하는 url 등록

```python
# crud/urls.py


urlpatterns = [
    # . . .
    path('accounts/', include('accounts.urls')),    # <----
]
```

- `accounts/` 폴더에 `urls.py` 파일 생성하고 다음 내용 작성

```python
# accounts/urls.py

from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [

]
```

## 2. Custom User Model 정의하기

- `AbstractUser`를 상속받는 `User` 모델 정의

```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- 기본 User 모델을 우리가 작성한 User 모델로 교체하기

```python
# crud/settings.py


AUTH_USER_MODEL = 'accounts.User'    # <---------- User 대문자 주의  
```

- admin 사이트에 등록하기

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

#### `User` 모델을 DB에 반영하기

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

- Admin 계정 생성하기
	- 차후에 로그인 테스트 계정으로 활용한다.
```shell
$ python manage.py createsuperuser
```

## 3. 로그인

#### `accounts/login/` url 추가

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),    # <----------
]
```

#### `login()` view 함수 작성

- `AuthenticationForm` 으로 로그인 폼 생성
- GET 요청 먼저 작성

```python
# accounts/views.py

from django.contrib.auth.forms import AuthenticationForm   # <---

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

#### 템플릿 작성

- `accounts/templates/accounts` 폴더 생성 및 `login.html`  생성

```html
  <!-- accounts/templates/login.html -->

  <h1>Login</h1>

  <form action="{% url "accounts:login" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Login">
  </form>
```

#### 로그인 요청 처리(POST)

- `login` 함수 완성하기
- **django** 에서 제공하는 `login` 함수를 `auth_login` 으로 가져오기

```python
from django.contrib.auth import login as auth_login  # <---주의  

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

- 메인 페이지(`index.html`)에  `login` 링크 추가

```html
<!-- articles/index.html -->

<a href="{% url "accounts:login" %}">Login</a> |
<a href="{% url "articles:create" %}">CREATE</a>
```

- 앞에서 생성한 Admin 계정으로 테스트 해보기
- `session` 테이블과 브라우저의 쿠키에서 `sessionid` 확인해보기

#### 사용자 이름 출력하기

- `request.user.username` 출력 하기

```html
<!-- artcles/index.html -->

<h3>{{ request.user }}님, 환영합니다!</h3>
<h3>{{ request.user.username }}님, 환영합니다!</h3>
```

- `request.user` 와 비교

----------

## 4. 로그아웃

#### `accounts/logout/` url 추가

```python
# accounts/urls.py

app_name = 'accounts'
urlpatterns = [
    # . . .
    path('logout/', views.logout, name='logout'),    # <----------
]
```

#### 로그아웃 요청(POST)

- `logout()` view 함수
- **django** 에서 제공하는 `logout` 함수를 `auth_logout` 으로 가져오기

```python
# accounts/views.py
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

#### 로그아웃 버튼 추가

```html
<form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
</form>
```

- `is_authenticated` 활용하기

```html
  <!-- articles/index.html -->

  {% if request.user.is_authenticated %}
    <!-- 로그인 사용자 -->
    <h3>{{ request.user }}님, 환영합니다!</h3>  
    <form action="{% url "accounts:logout" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="Logout">
    </form>
    <a href="{% url "articles:create" %}">CREATE</a>

  {% else %}
    <!-- 로그아웃 사용자 -->
    <a href="{% url "accounts:login" %}">Login</a> 
  {% endif %}
```

------------

