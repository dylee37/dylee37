# Authentication 2

[TOC]

-----------------------

## 1. `CustomUserCreationForm` , `CustomUserChangeForm` 정의

- `UserCreationForm`, `UserChangeForm` 에 설정된 기존 **auth.User** 모델을 현재 사용자 모델로 변경

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

## 2. 회원 가입

#### url 작성

```python
# accounts/urls.py

urlpatterns = [
    # . . .
    path('signup/', views.signup, name='signup'),
]
```

#### 회원 가입 폼 요청(GET)

- `signup()` view함수 작성

```python
# accounts/views.py
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```

- 회원가입 링크 추가

```html
<!-- articles의 index.html -->

  {% if request.user.is_authenticated %}     
   . . .
  {% else %}
    <a href="{% url "accounts:login" %}">Login</a> |
    <a href="{% url "accounts:signup" %}">회원가입</a> |
  {% endif %}
```

#### `signup.html` 작성

```html
<!-- accounts/templates/accounts/signup.html -->


  <h1>Signup</h1>

  <form action="{% url "accounts:signup" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Signup">
  </form>
```

#### 회원 가입 POST 요청 완성

- 회원가입과 동시에 로그인 진행

```python
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        # . . .
```

## 3. 회원 탈퇴

#### url 작성

```python
# accounts/urls.py

urlpatterns = [
    # . . .
    path('delete/', views.delete, name='delete')
]
```

#### view함수 작성

```python
# accounts/views.py
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')
```

#### 탈퇴 버튼 작성

```html
<!-- articles의 index.html -->
{% if request.user.is_authenticated %}
    <form action="{% url "accounts:delete" %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="회원탈퇴">
    </form>
```

## 4. 회원 정보 수정

#### url 작성

```python
# accounts/urls.py

urlpatterns = [
    # . . .
    path('update/', views.update, name='update'),
]
```

#### 회원 정보 수정폼 요청(GET)

- `signup()` view함수 작성

```python
# accounts/views.py
from .forms import CustomUserChangeForm
def update(request):
    if request.method == 'POST':
        pass
    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context), context)
```

#### `update.html` 작성

```html
<!-- accounts/templates/accounts/update.html -->
  <h1>Update</h1>

  <form action="{% url "accounts:update" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="수정">
  </form>
```

#### CustomUserChangeForm 수정

```python
# accounts/forms.py
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        # 보여줄 필드 선택
        fields = ('email', 'first_name', 'last_name', )()
```



#### 회원정보 수정 링크 추가

```html
<a href="{% url "accounts:update" %}">회원정보수정</a>
```



#### POST 요청 완성

```python
# accounts/forms.py

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, isinstance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # . . .
```

## 5. 비밀번호 변경

#### url 작성

```python
# accounts/urls.py

urlpatterns = [
    # . . .
    path('<int:user_pk>/password/', views.change_password, name='change_password'),
]
```

#### view함수 작성

```python
# accounts/views.py

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

#### `change_password.html` 작성

```python
# accounts/templates/accounts/change_password.html
  <h1>Change Password</h1>
  
  <form action="{% url "accounts:change_password" %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="변경">
  </form>
```
