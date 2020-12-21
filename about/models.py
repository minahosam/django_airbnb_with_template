from django.db import models
from ckeditor.fields import RichTextField
class About(models.Model):
    what_we_do=RichTextField(max_length=1000)
    goal=RichTextField(max_length=1000)
    mission=RichTextField(max_length=1000)
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = 'about'
        verbose_name_plural = 'abouts'
class faq(models.Model):
    title=models.CharField(max_length=500)
    description=RichTextField(max_length=100000)
    def __str__(self):
        return self.title
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'