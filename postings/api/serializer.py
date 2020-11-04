from postings.models import BlogPost
from rest_framework import serializers


class BlogPostSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = BlogPost
        fields = ['pk', 'user', 'title', 'content', 'timestamp']
        read_only_fields = ["pk", "timestamp", "user"]

    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("Post with this title already exists.")
        else:
            return value