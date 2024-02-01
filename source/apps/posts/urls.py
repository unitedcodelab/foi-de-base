from django.urls import path

from . import views


urlpatterns = [
    # path("feed/", views.feed, name="feed"),

    path("criar/", views.create_post, name="create_post"),
    
    path("<str:slug>/", views.get_unknown_user_post, name="get_unknown_user_post"),
    path("<str:slug>/comentarios/criar/", views.create_comment, name="create_comment"),
    
    path("<str:student_nick>/", views.get_all_student_posts, name="get_all_student_posts"),
    path("<str:student_nick>/<str:slug>/", views.get_single_student_post, name="get_single_student_post"),
]
