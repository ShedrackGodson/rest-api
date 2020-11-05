from .serializer import BlogPostSerializer
from rest_framework import generics, mixins
from postings.models import BlogPost
from django.db.models import Q


class BlogPostListView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(title__icontains=query) | Q(content__icontains=query)).distinct()
        return qs
    
    def post(self, request, *args, **kwargs): # Giving the ListAPIView ability to Create
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
    # def put(self, request, *args, **kwargs): # Giving the ListAPIView ability to Create
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs): # Giving the ListAPIView ability to Create
    #     return self.update(request, *args, **kwargs)
    
    # def delete(self, request, *args, **kwargs):
    #     print("Delete Fired!")
    
    

class BlogPostCreateView(generics.CreateAPIView):
    lookup_field = "pk"
    serializer_class = BlogPostSerializer
    # form = AddBlogPostForm()

    def get_queryset(self):
        return BlogPost.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostUpdateView(generics.UpdateAPIView):
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return BlogPost.objects.get(pk=pk)


class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = BlogPostSerializer
    # form = AddBlogPostForm()

    def get_queryset(self):
        return BlogPost.objects.all()
    
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return BlogPost.objects.get(pk=pk)