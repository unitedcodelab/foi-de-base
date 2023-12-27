from django.urls import path

from . import views


urlpatterns = [
    path("criar/", views.create_post, name="create_post"),
    path('feed/', views.feed, name="feed"),

    path('<str:student_nick>/', views.get_student_posts, name="get_student_posts"),
    path('<str:student_nick>/<str:slug>/', views.get_post, name="get_post"),
    path('unknown/<str:slug>/', views.get_post, name="get_post"),
]
