from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

# Create your models here.

"""
공모전 모델
"""


class Contest(models.Model):

    # 공모전 이름
    contest_name = models.CharField(max_length=100, null=False)
    # 공모전 주최 기관
    contest_organizer = models.CharField(max_length=100, null=False)
    # 작성자
    # author = models.ForeignKey('User', on_delete = models.CASCADE, related_name='contest_set')
    # 작성 제목
    title = models.CharField(max_length=100, null=False)
    # 마감 기한
    deadline = models.DateField()
    # 공모전 카테고리
    category = models.CharField(max_length=100, null=False)
    # 공모전 포스터
    poster = models.ImageField(null=True)
    # 공모전 디테일 - ckeditor
    # detail = RichTextUploadingField()
    # 모집중인지 아닌지
    on_recruiting = models.BooleanField(default=True)
    # 전체 구하는 팀원 수
    # total_members = models.IntegerField()
    # 현제 우리 팀원 수
    # confirmed_members = models.IntegerField()
    hit_count = models.PositiveIntegerField(default=0)
    timeline = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contest_name + "/" + self.title

    @property
    def update_hit_counter(self):
        self.hit_count += 1
        self.save()


"""
공모전 참가자의 역할에 해당하는 모델
"""


class Role(models.Model):

    # 역할 이름
    name = models.CharField(max_length=100, null=False)
    # 연결된 공모전
    contest = models.ForeignKey(
        "Contest", on_delete=models.CASCADE, related_name="role_set"
    )
    # 수락된 팀원들
    # confirmed_members = models.ManyToManyField(User)
    # 수락 대기중인 사용자들
    # not_confirmed_members = models.ManyToManyField(User)
