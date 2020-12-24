from django.contrib import admin
from . import models
class roomTabular(admin.StackedInline):
    model=models.RoomImage
class roomsearch(admin.ModelAdmin):
    list_display=['title','price','location','check_aviability']
    inlines=[roomTabular,]
    prepopulated_fields={'slug':['title']}
admin.site.register(models.Room,roomsearch)
class roombook(admin.ModelAdmin):
    list_display=['room_reserve']
admin.site.register(models.RoomBook)
admin.site.register(models.RoomImage)
admin.site.register(models.RoomReview)
admin.site.register(models.category)