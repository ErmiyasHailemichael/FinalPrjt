from .models import Blog
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('author', 'id', 'title', 'pub_date', 'body', 'created_on')
        