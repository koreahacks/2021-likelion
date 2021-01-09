from django.shortcuts import render, redirect
from .models import Contest, Role

# Create your views here.

"""
공모전 생성
입력값을 불러와 새로운 공모전 모델 생성
"""


def create_contest(request):

    if request.user.is_authenticated:
        current_user = request.user
    else:
        pass
        # return redirect('login')

    if request.method == "POST":

        # 새로운 객체 생성
        new_contest = Contest()

        # 템플릿으로부터 데이터를 불러오는 코드
        new_contest.author = current_user
        new_contest.contest_name = request.POST["contest_name"]
        new_contest.contest_organizer = request.POST["contest_organizer"]
        new_contest.title = request.POST["title"]
        new_contest.deadline = request.POST["deadline"]
        new_contest.category = request.POST["category"]

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

        return redirect("contest_list")

    return render(request, "contest_create.html")


"""
공모전의 리스트를 불러오는 함수
검색 기능, 키워드 별로 정렬 해주는 기능 필요
"""

# 정렬, 검색 둘다 한번에 할 수 있으면 최고 , 안되면 어쩔 수 없음
def display_contest_list(request):

    # search bar 구현
    if "search" in request.GET:
        search_keyword = request.GET["search"]
        print(search_keyword)
        filtered_contests = Contest.objects.filter(
            contest_name__contains=search_keyword
        )
        print(len(filtered_contests))
        context = {"contests": filtered_contests}
        return render(request, "contest_list.html", context)

    # 기본 정렬 기준 : 생성 시간
    contest_query_set = Contest.objects.order_by("timeline")

    if "sort" in request.GET:
        if request.GET.get("sort") == "hit":
            keyword = "hit_count"
        elif request.GET.get("sort") == "days":
            keyword = "days_left"
        else:
            keyword = "timeline"

        contest_query_set = Contest.objects.order_by(keyword)

    context = {"contests": contest_query_set}

    return render(request, "contest_list.html", context)


"""
불러온 공모전 데이터를 삭제하는 함수
"""


def delete_contest(request, contest_id):

    contest = Contest.objects.get(pk=contest_id)
    contest.delete()
    redirect("contest_list")
