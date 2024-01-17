from django.urls import path

from .views import index, post

urlpatterns = [
    path("", index, name="blog-index"),
    path("post-<str:post_number>/", post, name="blog-post"),
]
