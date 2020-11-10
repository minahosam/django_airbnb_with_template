from django.contrib import admin
from . import models
class roomTabular(admin.StackedInline):
    model=models.RoomImage
class roomsearch(admin.ModelAdmin):
    list_display=['title','price','location']
    inlines=[roomTabular,]
admin.site.register(models.Room,roomsearch)
admin.site.register(models.RoomBook)
admin.site.register(models.RoomImage)
admin.site.register(models.RoomReview)
admin.site.register(models.category)