from django.db import models
from django.db.models.aggregates import Max, Min
from django.db.models.fields import CharField, SlugField
from django.utils.datetime_safe import datetime
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
class Room(models.Model):
    owner=models.ForeignKey(User, related_name='room_owner', on_delete=models.CASCADE,verbose_name=_('owner'))
    title = models.CharField(_('title'),max_length=100)
    price = models.IntegerField(_('price'),default=0)
    description = RichTextField(_('description'))
    loction_in_detail=models.CharField(_('location_in_detail'),max_length=500,null=True,blank=True,help_text=_('this is help text'))
    location = models.ForeignKey('places',related_name='room_location',on_delete=models.CASCADE,null=True,blank=True,verbose_name=_('location'))
    image=models.ImageField( _('image'),upload_to='property/')
    category = models.ForeignKey('category', related_name='room_category', on_delete=models.CASCADE,verbose_name=_('category'))
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
        starting_reservation=Room.room_book.from_date()
        all_reservations=self.room_book.all()
        print(all_reservations)
        ended_reservation=self.to_date
        for reserve in all_reservations:
            print(reserve)
            if starting_reservation > reserve.from_date and ended_reservation < reserve.to_date:
                return 'room is booked'
            elif starting_reservation < reserve.from_date and ended_reservation > reserve.to_date:
                return 'room is booked'
        else:
            return 'aviable'
    def all(self):
        all_reservation=self.room_book.all()
        return all_reservation
    def get_avg(self):
        all_reviews=self.room_review.all()
        all_ratings=0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review.rate
                print(all_ratings)
            return all_ratings/len(all_reviews)
        else:
            return '------'
class places(models.Model):
    location_name=models.CharField(max_length=5000,null=True,blank=True)
    image=models.ImageField( upload_to='places/')
    def __str__(self):
        return(self.location_name)
class RoomImage(models.Model):
    room= models.ForeignKey(Room, related_name='room_image', on_delete=models.CASCADE)
    main_image=models.ImageField( upload_to='room_image/')
    def __str__(self):
        return str(self.room)
class category(models.Model):
    name=models.CharField( max_length=500,blank=True, null=True)
    icon=models.CharField(max_length=500,blank=True,null=True)
    icon_image=models.ImageField(upload_to='icon_image',null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'
class RoomReview(models.Model):
    room=models.ForeignKey(Room,related_name="room_review", on_delete=models.CASCADE)
    author=models.ForeignKey(User,related_name='feedback_author',on_delete=models.CASCADE)
    eat_rate=models.IntegerField(default=0)
    cleaning_rate=models.IntegerField(default=0)
    rate=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    feedback = models.TextField(null=True,blank=True )
    def __str__(self):
        return str(self.room)
class RoomBook(models.Model):
    room= models.ForeignKey(Room, related_name='room_book', on_delete=models.CASCADE)
    name=models.ForeignKey(User,related_name='book_user',on_delete=models.CASCADE)
    email=models.EmailField( max_length=254)
    from_date=models.DateField(default=timezone.now)
    to_date=models.DateField(default=timezone.now)
    guest=models.IntegerField(default=1)
    children=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
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