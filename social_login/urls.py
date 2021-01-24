from django.urls import path
from . import views
app_name='social'
urlpatterns = [
     path('facebook/', views.FacebookLogin.as_view(), name='fb_login')
]
