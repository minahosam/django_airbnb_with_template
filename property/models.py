from django.db import models
from django.utils.datetime_safe import datetime
from django.utils import timezone
class Room(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=5000)
    location = models.CharField( max_length=5000)
    image=models.ImageField( upload_to='property/', height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey('category', related_name='room_category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
class RoomImage(models.Model):
    room= models.ForeignKey(Room, related_name='room_image', on_delete=models.CASCADE)
    main_image=models.ImageField( upload_to='room_image/')
    def __str__(self):
        return str(self.room)
class category(models.Model):
    name=models.CharField( max_length=500,blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'
class RoomReview(models.Model):
    room=models.ForeignKey(Room,related_name=("room_review"), on_delete=models.CASCADE)
    rate=models.IntegerField(default=0)
    feedback=models.TextField(null=True,blank=True )
    def __str__(self):
        return str(self.room)
class RoomBook(models.Model):
    room= models.ForeignKey(Room, related_name='room_book', on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    guest=models.IntegerField(default=1)
    children=models.IntegerField(default=0)
    def __str__(self):
        return self.name
    