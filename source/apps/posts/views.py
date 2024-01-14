from django.shortcuts import HttpResponse, render, get_object_or_404

from .models import *

from .utils.create_slug import create_slug
from .utils.verifications.create_post import Verifications


def feed(request):
    context = {}

    # if request.method == "GET":
    #     posts = Post.objects.filter(
    #         author=request.user.student
    #     )

    # context = {
    #     "posts": posts
    # }

    return render(request, 'pages/posts/feed.html', **context)


def get_student_posts(request, student_nick):
    student = get_object_or_404(Student, nick=student_nick)
    posts = Post.objects.filter(author=student)

    context = {
        "posts": posts
    }
    return render(request, 'pages/posts/students/posts.html', context)


def get_post(request, student_nick, slug):
    post = get_object_or_404(Post, slug=slug)
    success, _ = Verifications.get_post(post, student_nick)
    if not success:
        return HttpResponse(status=400)

    context = {
        "post": post
    }
    return render(request, 'pages/posts/post.html', context)


def create_post(request):
    if request.method == "POST":
        success, _ = Verifications.create_post(request.POST)
        if not success:
            return HttpResponse(status=400)

        slug = create_slug(title=request.POST["title"])

        try:
            author = Student.objects.get(user=request.user)
        except:
            author = None

        Post.objects.create(
            slug=slug,
            title=request.POST["title"],
            content=request.POST["content"],
            author=author
        )

        return render(request, "pages/posts/post.html")

    return render(request, "pages/posts/create.html")
