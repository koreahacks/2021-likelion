from django.urls import path
from . import views

urlpatterns = [
    path('user_login/', views.user_login ,name="user_login"),
    path('portfolio_detail/<int:pk>', views.user_detail.as_view(),
         name="portfolio_detail"),  # 유저 포트폴리오 개인 페이지 이동
    path('portfolio/', views.user_list.as_view(),
         name="portfolio_list"),  # 유저 포트폴리오 리스트
]