from django.shortcuts import render
# 장고에서 일치하는 패턴을 찾으면, HttpRequest 객체를 첫번째로 인수하고, 경로로 특정 view 함수를 호출함
from django.http import HttpResponse

# Create your views here.

# views
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# views에서 작성한 후, urls.py 파일에 경로 설정만 해주면 됨
def urlTest(request):
    return HttpResponse("Url Test")