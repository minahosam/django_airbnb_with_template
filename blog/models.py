from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager
class Post(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=10000)
    tags=TaggableManager()
    image=models.ImageField(upload_to='posts/')
    created_at=models.DateTimeField(default=timezone.now().date)
    author=models.ForeignKey(User,related_name='post_author',on_delete=models.CASCADE)
    comments=''
    search=''
    views_count=models.IntegerField(default=0)
    category = models.ForeignKey('category', related_name='room_category', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
class category(models.Model):
    name=models.CharField( max_length=500,blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'categories'