from .models import Room,RoomReview
from rest_framework import serializers
class roomserializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields=['owner','title','price','description','location','image','category']
class roomreviewserializer(serializers.ModelSerializer):
    class Meta:
        model=RoomReview
        fields=['room','rate','feedback']