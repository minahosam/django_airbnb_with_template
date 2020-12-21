from rest_framework import serializers
from .models import Post
class postserializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['title']