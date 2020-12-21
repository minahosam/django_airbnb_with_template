from django.urls import path
from .views import blog_list,blog_detail
from .api_view import api_list,api_detail
app_name='blog'
urlpatterns = [
    path('',blog_list.as_view(),name='listing'),
    path('<int:pk>/',blog_detail.as_view(),name='detail'),
    path('api_l/',api_list,name='api_l'),
    path('api_d/<int:pk>',api_detail,name='api_d'),
]