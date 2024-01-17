from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def post(request, post_number):
    return render(request, f"blog/post{post_number}.html")
