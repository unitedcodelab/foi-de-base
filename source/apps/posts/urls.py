from django.urls import path
from .views import feed
from . import views

urlpatterns = [
    path("criar/", views.create_post, name="create_post"),
    path('feed/', feed)
]
