import random
from django.shortcuts import render

# Create your views here.


# articles/ 요청이 들어오면 호출되는 함수
def index(request):
    context = {
        'name': 'Jane',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,        
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


# 사용자 입력 데이터를 추출해서 응답 페이지에 보여주기
def catch(request):
    # 사용자 입력데이터는 대체 어디에 있을까? -> request 객체
    print(request.GET)  # <QueryDict: {'message': ['ssafy']}>
    print(request.GET.get('message'))  # ssafy
    context = {
        'message': request.GET.get('message'),
    }
    return render(request, 'articles/catch.html', context)




def detail(request, num):
    context = {
        'num': num,
    }
    return render(request, 'articles/detail.html', context)


def greeting(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/greeting.html', context)
