from django.db import models
from django.utils.datetime_safe import datetime
from django.utils import timezone
class Room(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=5000)
    location = models.CharField( max_length=5000)
    image=models.ImageField( upload_to='property/', height_field=None, width_field=None, max_length=None)
class RoomImage(models.Model):
    room= models.ForeignKey(Room, related_name='room_image', on_delete=models.CASCADE)
    main_image=models.ImageField( upload_to='room_image/')
class category(models.Model):
    name=models.CharField( max_length=50)
class RoomReview(models.Model):
    room=models.ForeignKey(Room,related_name=("room_review"), on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    feedback=models.TextField(null=True,blank=True )
class RoomBook(models.Model):
    room= models.ForeignKey(Room, related_name='room_book', on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    guest=models.IntegerField(default=1)
    children=models.IntegerField(default=0)