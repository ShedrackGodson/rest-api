from postings.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = BlogPost
        fields = ['pk', 'user', 'title', 'content', 'timestamp']