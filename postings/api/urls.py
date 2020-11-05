from django.urls import path
from .views import (
        BlogPostRudView, BlogPostCreateView, BlogPostListView, BlogPostUpdateView
    )

urlpatterns = [
    path("create/", BlogPostCreateView.as_view(), name="blog-post-create"),
    path("update/<int:pk>/", BlogPostUpdateView.as_view(), name="blog-post-update"),
    path("list/", BlogPostListView.as_view(), name="blog-post-list"),
    path("<int:pk>/", BlogPostRudView.as_view(), name="blog-post-rud"),
]