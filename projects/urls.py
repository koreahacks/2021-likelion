from django.urls import path
from . import views

''' 포트폴리오 생성/수정 및 디테일 페이지 URL'''
urlpatterns = [
    path('project_edit/', views.project_edit, name='project_edit'),
    path('project_detail/', views.project_detail, name='project_detail'),
]