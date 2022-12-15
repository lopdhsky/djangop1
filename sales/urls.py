from django.urls import path
from .views import 세일목록, 세일상세, 세일_입력

app_name = "홈페이지" # url의 namespace와 달라도 된다 지정해주는 것이 중요

urlpatterns = [
    path('', 세일목록),
    path('<int:pk>/', 세일상세), # int하는 이유 : 안하면 pk가 숫자라서 그아래 모든문자도 숫자로만 받아야한다
    path('make/', 세일_입력),
    
]
