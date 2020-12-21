from django.db import models
class Info (models.Model):
    title=models.CharField(max_length=20)
    image=models.ImageField(upload_to='info/')
    description=models.TextField(max_length=200)
    fb_link=models.URLField(max_length=200)
    twitter_link=models.URLField(max_length=200)
    instgram_link=models.URLField(max_length=200)
    address=models.TextField(max_length=2000)
    phone_number=models.CharField(max_length=20)
    mail=models.EmailField(max_length=100)
    def __str__(self):
        return(self.title)
    