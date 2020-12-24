from .models import Room,RoomReview
from .serializer import roomreviewserializer,roomserializer 
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.permissions import IsAuthenticated
class room_l(ListAPIView,CreateAPIView):
    model=Room
    serializer_class=roomserializer
    queryset=Room.objects.all() 
    permission_classes=[IsAuthenticated]
class room_d(RetrieveUpdateDestroyAPIView):
    model=Room
    serializer_class=roomserializer
    queryset=Room.objects.all()  
    permission_classes=[IsAuthenticated]