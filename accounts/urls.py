from django.urls import path
from .views import profile , profile_edit , signup , user_reservation,rate_feedback,show_my_listing


app_name = 'accounts'

urlpatterns = [
    path('signup',signup , name='signup'),
    path('profile/',profile,name='profile'),
    path('profile/reservation',user_reservation,name='user_reservation'),
    path('profile/reservationl/add_feedback/<slug:slug>',rate_feedback,name='rate_feedback'),
    path('profile/edit', profile_edit , name='profile_edit'),
    path('listing',show_my_listing,name='listing'),
]
