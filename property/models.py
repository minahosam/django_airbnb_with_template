from django.db import models
from django.db.models.fields import SlugField
from django.utils.datetime_safe import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
class Room(models.Model):
    owner=models.ForeignKey(User, related_name='room_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = RichTextField()
    location = models.CharField( max_length=5000)
    image=models.ImageField( upload_to='property/')
    category = models.ForeignKey('category', related_name='room_category', on_delete=models.CASCADE)
    slug=models.SlugField(null=True,blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        super(Room, self).save(*args, **kwargs) # Call the real save() method
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'room'    
        verbose_name_plural = 'rooms'
        ordering=['price']
    def get_absolute_url(self):
        return reverse ( 'rooms:detail', kwargs={'slug': self.slug })
    def check_aviability(self):
        all_reservations=self.room_book.all()
        print(all_reservations)
        starting_reservation=self.room_book.from_date
        ended_reservation=self.to_date
        for reserve in all_reservations:
            print(reserve)
            if starting_reservation > reserve.from_date and ended_reservation < reserve.to_date:
                return 'room is booked'
            elif starting_reservation < reserve.from_date and ended_reservation > reserve.to_date:
                return 'room is booked'
        else:
            return 'aviable'
    #def all(self):
    #    all_reservation=self.room_book.all()
    #    return all_reservation
    
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
    room=models.ForeignKey(Room,related_name="room_review", on_delete=models.CASCADE)
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
    #def room_reserve(self):
        all_reservation=self.room.all
        starting_reserve=self.from_date()
        ending_reserve=self.to_date()
        for reserve in all_reservation:
            if starting_reserve > reserve and ending_reserve < reserve:
                return 'room is booked'
            elif starting_reserve < reserve and ending_reserve > reserve:
                return 'room is booked'
        else:
            return 'aviable'