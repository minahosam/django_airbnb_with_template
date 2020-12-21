from .models import Room,RoomReview
from .serializer import roomreviewserializer,roomserializer 
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
class room_l(ListAPIView,CreateAPIView):
    model=Room
    serializer_class=roomserializer
    queryset=Room.objects.all() 
class room_d(RetrieveUpdateDestroyAPIView):
    model=Room
    serializer_class=roomserializer
    queryset=Room.objects.all()  