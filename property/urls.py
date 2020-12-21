from property.views import roomdetail
from django.urls import path
from . import views
from .api_view import room_l,room_d
app_name='property'
urlpatterns = [
    path('',views.roomlist.as_view(),name='list'),
    path('<slug>/',views.roomdetail.as_view(),name='detail'),
    path('api_ll',room_l.as_view(),name='room_list'),
    path('api_d/<pk>',room_d.as_view(),name='room_detai')
]
