from django.shortcuts import render

from .models import *
from .utils.create_slug import create_slug


def create_post(request):
    if request.method == "POST":
        try: author = request.user.student
        except: author = None #AnnonymousUser

        slug = create_slug(
            title=request.POST["title"]
        )

        post = Post.objects.create(
            slug=slug,
            title=request.POST["title"],
            description=request.POST["content"],
            author=author
        )        
        post.save()

        # redirect to post

    return render(request, "pages/posts/create.html")
