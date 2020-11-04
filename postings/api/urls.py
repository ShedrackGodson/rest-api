from django.urls import path
from .views import BlogPostRudView, BlogPostView, BlogPostListView

urlpatterns = [
    path("create/", BlogPostView.as_view(), name="blog-post-create"),
    path("list/", BlogPostListView.as_view(), name="blog-post-list"),
    path("<int:pk>/", BlogPostRudView.as_view(), name="blog-post-rud"),
]