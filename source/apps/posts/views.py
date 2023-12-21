from django.shortcuts import render


def feed(request):
    return render(request, '../templates/pages/posts/feed.html')
