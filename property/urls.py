from property.views import roomdetail
from django.urls import path
from . import views
app_name='property'
urlpatterns = [
    path('',views.roomlist.as_view(),name='list'),
    path('/<pk>',views.roomdetail.as_view(),name='detail'),
]
