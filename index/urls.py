from django.contrib import admin
from django.urls import path
from .views import home , room_search , search_by_category
app_name = 'index'
urlpatterns = [
    path('',home,name='home'),
    path('room_search',room_search,name='room_search'),
    path('<category_name>',search_by_category,name='category')
]
