from .serializer import BlogPostSerializer
from rest_framework import generics
from postings.models import BlogPost


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)