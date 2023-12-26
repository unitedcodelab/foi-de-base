from django.shortcuts import render

from .models import *

from .utils.create_slug import create_slug
from .utils.verifications.create_post import Verifications 



def feed(request):
    return render(request, 'pages/posts/feed.html')


def get_post(request):
    context = {}

    posts = Post.objects.filter(
        author=request.user.student
    )
    context = {
        "posts": posts
    }
    return render(request, 'pages/posts/feed.html', context)


def create_post(request):
    if request.method == "POST":
        success, message = Verifications.create_post(request.POST)
        if not success:
            return render(request, "pages/posts/create.html", {
                "error": {
                    "message": message,
                }
            }, status=400)

        slug = create_slug(title=request.POST["title"])

        try: author = Student.objects.get(user=request.user)
        except: author = None

        Post.objects.create(
            slug=slug,
            title=request.POST["title"],
            content=request.POST["content"],
            author=author
        )

        # redirect to post

    return render(request, "pages/posts/create.html")
