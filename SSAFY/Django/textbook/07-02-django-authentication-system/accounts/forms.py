from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Django는 User 모델을 직접 참조하는 것을 권장하지 않는다.
# from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # get_user_model 함수는 현재 프로젝트에 활성화 되어있는 유저 클래스를 자동으로 반환
        model = get_user_model()
        # model = User
