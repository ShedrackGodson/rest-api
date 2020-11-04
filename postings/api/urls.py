from django.urls import path
from .views import BlogPostRudView, BlogPostView

urlpatterns = [
    path("create/", BlogPostView.as_view(), name="blog-post-create"),
    path("<int:pk>/", BlogPostRudView.as_view(), name="blog-post-rud"),
]