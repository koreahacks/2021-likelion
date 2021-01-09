from django.shortcuts import render

# Create your views here.


def create_contest(request):

    return render(request, "contest_create.html")
