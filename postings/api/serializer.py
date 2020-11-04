from postings.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = BlogPost
        fields = ['pk', 'user', 'title', 'content', 'timestamp']
        read_only_fields = ["pk", "timestamp"]

        def validate_title(self, value):
            qs = BlogPost.objects.filter(title__iexact=value)
            if qs.exists():
                raise serializers.ValidationError("Title must be unique.")
            else:
                return value