from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def login(request):
    """
    사용자 로그인을 처리하는 뷰 함수
    GET: 로그인 폼을 보여줌
    POST: 로그인 인증을 처리함
    """
    # POST 요청인 경우 (사용자가 로그인 폼을 제출했을 때)
    if request.method == 'POST':
        # AuthenticationForm: Django 내장 폼으로 username과 password를 검증
        # 첫 번째 인자로 request, 두 번째 인자로 POST 데이터를 받음
        form = AuthenticationForm(request, request.POST)

        # 폼 검증: username과 password가 올바른지 확인
        if form.is_valid():
            # form.get_user(): 인증된 사용자 객체를 반환
            # auth_login(): Django의 로그인 함수로 세션을 생성하여 로그인 상태 유지
            # - 세션 ID를 쿠키에 저장
            # - 서버의 세션 테이블에 사용자 정보 저장
            auth_login(request, form.get_user())

            # 로그인 성공 후 게시글 목록 페이지로 리다이렉트
            return redirect('articles:index')

    # POST가 아닌 요청인 경우 (사용자가 로그인 페이지에 처음 접속했을 때)
    else:
        # 빈 로그인 폼 생성
        form = AuthenticationForm()

    # 템플릿에 전달할 데이터를 딕셔너리로 구성
    context = {
        'form': form,  # 로그인 폼 (GET일 때는 빈 폼, POST 실패 시에는 에러 메시지 포함)
    }

    # 로그인 페이지 템플릿을 렌더링하여 응답
    # - GET 요청: 빈 로그인 폼 표시
    # - POST 요청 실패: 에러 메시지와 함께 폼 다시 표시
    return render(request, 'accounts/login.html', context)
