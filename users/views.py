from django.shortcuts import render,redirect

# CBV import
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.views.generic.list import ListView

# Model Import
from .models import User

# 포트폴리오 리스트 페이지
class portfolio_list(ListView):
    '''포트폴리오(유저) 디테일'''
    model = User
    paginate_by = 9
    context_object_name = 'users'
    template_name = 'portfolio_list.html'

# 유저 포트폴리오 페이지
class portfolio_detail(DetailView):
    '''포트폴리오(유저) 디테일'''
    model = User
    context_object_name = 'users'
    template_name = 'portfolio_detail.html' 

# User Login View
def user_login(request):
    # POST 형식의 로그인 폼 값 전달 시에 함수 실행
    if request.method == 'POST'
        username = request.POST['username']
        password = request.POST['password']

        # 입력한 username과 password 가 서버에 있는 회원인지 확인하는 함수.
        # 이 결과 (회원이다. 아니다.) 를 user 에 넣어준다.
        # 찾아서 id, paasword 일치하는 지 확인
        user = auth.authenticate(request, username=username, password=password)

        # 로그인 됐을 시 none이 아니기 때문에, 메인으로 이동해야함!
        if user is not None:
            auth.login(request, user)
            # return redirect('') # 메인으로 이동해야함.

        # 로그인 안됐을 시, 오류 안내
        else:
            print("로그인 실패")
            return redirect('user_login')
   
    #Login Form으로 이동 할 시 기본 로그인 창으로 이동함.
    else:
        return render(request, "userLogin.html")

