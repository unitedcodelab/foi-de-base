from django.shortcuts import HttpResponse, render, redirect, get_object_or_404

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

    return render(request, 'pages/posts/feed.html', context)


def get_all_student_posts(request, student_nick):
    student = get_object_or_404(Student, nick=student_nick)
    posts = Post.objects.filter(author=student)

    return render(request, 'pages/posts/students/posts.html', {
        "posts": posts
    })


def get_single_student_post(request, student_nick, slug):   
    post = get_object_or_404(Post, slug=slug)

    success, message = Verifications.get_post(post, student_nick)
    if not success:
        print(message)
        return HttpResponse(status=400)

    return render(request, 'pages/posts/post.html', {
        "post": post
    })

def get_unknown_user_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'pages/posts/post.html', {
        "post": post
    })


def create_post(request):
    if request.method == "POST":
        success, message = Verifications.create_post(request.POST)
        if not success:
            print(message)
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

        if author is None: 
            return redirect(f"/posts/{slug}")
        
        return redirect(f"/posts/{author.nick}/{slug}")

    return render(request, "pages/posts/create.html")


def create_comment(request, slug):
    if request.method == "POST":
        """ success, message = Verifications.create_comment(request.POST)
        if not success:
            print(message)
            return HttpResponse(status=400) """

        post = get_object_or_404(Post, slug=slug)

        try:
            author = Student.objects.get(user=request.user)
        except:
            author = None

        if request.POST["parent"] == "None":
            parent = None
        else:
            parent = get_object_or_404(Comment, id=int(request.POST["parent"]))

        Comment.objects.create(
            content=request.POST["content"],
            author=author,
            parent=parent,
            post=post
        )

        return HttpResponse(status=201)

    return HttpResponse(status=405)