from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    return render(request, 'articles/index.html')
