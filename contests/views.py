from django.shortcuts import render
from .models import Contest, Role

# Create your views here.

"""
공모전 생성
입력값을 불러와 새로운 공모전 모델 생성
"""


def create_contest(request):

    if request.method == "POST":

        # new_contest = Contest()

        contest_name = request.POST["contest_name"]
        contest_organizer = request.POST["contest_organizer"]
        title = request.POST["title"]
        deadline = request.POST["deadline"]
        category = request.POST["category"]

        # 불러온 데이터 저장하는 코드 필요

        print(contest_name, contest_organizer, title, deadline, category)

        # request.POST => csrt_token + 공모전 입력값들 + 역할 개수
        number_of_roles = len(request.POST) - 6

        print(number_of_roles)

        for i in range(number_of_roles):

            # 역할 obj 생성 후 공모전 연결까지 하는 코드 필요

            index = "role_name_" + str(i)
            role_name = request.POST[index]
            print(role_name)

        poster = request.FILES["poster"]
        print(poster)

    return render(request, "contest_create.html")


def display_contest_list(request):
    pass
