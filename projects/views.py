from django.shortcuts import render
from .forms import CreateProject
from .models import Project, ProjectTags

# 유저 프로젝트 Edit Page
def project_edit(request):
    form = CreateProject()
    return render(request, 'project_edit.html', {"form": form})

# 유저 프로젝트 디테일 페이지
def project_detail(request):
    if request.method == "POST":
        # 프로젝트 생성하기
        s1 = request.POST.get('description').split("src=")
        s2 = s1[1].split('"')
        project = Project(
            title=request.POST.get('title'),
            project_date=request.POST.get('project_date'),
            position=request.POST.get('position'),
            description=request.POST.get('description'),
            user=request.user,
            thumnail=s2[1]
        )
        project.save()

        # 태그 생성하기
        tags = request.POST.get('tags').split(',')
        for tag in tags:
            tg = ProjectTags(
                name=tag,
                projectid=project
            )
            tg.save()

    # 리스트 포폴
    project1 = Project.objects.all()
    tag = ProjectTags.objects.all()

    # print(description)
    return render(request, 'project_detail.html', {
        "project": project1,
        "tags": tag
    })

