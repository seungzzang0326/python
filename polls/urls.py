from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # 가장 상위 urls.py 경로 설정에서 ex) 'polls/' 이렇게 작성해서 / 붙일 필요 없는 것
    path('url_test', views.urlTest, name='url_test')
]
