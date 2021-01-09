from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_contest, name="contest_create"),
    path("list/", views.display_contest_list, name="contest_list"),
    path("<int:contest_id>/delete/", views.delete_contest, name="contest_delete"),
]
