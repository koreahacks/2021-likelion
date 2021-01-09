from django.shortcuts import render, redirect
from .models import Contest, Role

# Create your views here.

"""
공모전 생성
입력값을 불러와 새로운 공모전 모델 생성
"""


def create_contest(request):

    if request.method == "POST":

        # 새로운 객체 생성
        new_contest = Contest()

        # 템플릿으로부터 데이터를 불러오는 코드
        new_contest.contest_name = request.POST["contest_name"]
        new_contest.contest_organizer = request.POST["contest_organizer"]
        new_contest.title = request.POST["title"]
        new_contest.deadline = request.POST["deadline"]
        new_contest.category = request.POST["category"]
        new_contest.poster = request.FILES["poster"]

        new_contest.save()

        # request.POST => csrt_token + 공모전 입력값들 + 역할 개수
        number_of_roles = len(request.POST) - 6

        print(number_of_roles)

        for i in range(number_of_roles):

            new_role = Role()

            new_role.contest = new_contest

            index = "role_name_" + str(i)
            new_role.name = request.POST[index]

            new_role.save()

        return redirect("contest_create")

    return render(request, "contest_create.html")


def display_contest_list(request):

    # 기본 정렬 기준 : 생성 시간
    contest_query_set = Contest.objects.order_by("timeline")

    context = {"contests": contest_query_set}

    return render(request, "contest_list.html", context)
