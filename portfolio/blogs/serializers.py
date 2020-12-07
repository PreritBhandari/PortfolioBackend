from rest_framework import serializers
from .models import Blog


class ListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'category', 'subtitle', 'post', 'date_posted']
        read_only_fields = ['id']
