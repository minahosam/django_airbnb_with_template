from django.contrib import admin
from . import models
admin.site.register(models.Room)
admin.site.register(models.RoomBook)
admin.site.register(models.RoomImage)
admin.site.register(models.RoomReview)
admin.site.register(models.category)