from django.shortcuts import render
from property.models import places , Room ,category
from django.db.models import Q,Count
from django.contrib.auth.models import User
from blog.models import Post    
def home(request):
    place=places.objects.all().annotate(room_count=Count('room_location'))
    categories=category.objects.all()
    users_count=User.objects.all().count()
    destination_places=places.objects.all().count()
    hotels=Room.objects.filter(category__name='Hotel').count()
    resturants=Room.objects.filter(category__name='Resturant').count()
    post=Post.objects.all()[:3]
    popular_hotels=Room.objects.filter(category__name='Hotel')
    popular_resturant=Room.objects.filter(category__name='Resturant')
    popular_shopping=Room.objects.filter(category__name='Shopping')
    return render(request,'index/index.html',{'place':place , 'categories':categories , 'users_count':users_count , 'destination_places':destination_places ,
    'hotels':hotels , 'resturants':resturants , 'post':post , 'popuar_hotels':popular_hotels , 'popular_resturant':popular_resturant , 'popular_shopping':popular_shopping})
def room_search(request):
    tittle=request.GET.get('search_name','')
    loc=request.GET.get('search_place')
    print(tittle,loc)
    result=Room.objects.filter(Q(title__icontains=tittle) & Q(location__location_name__icontains=loc))
    return render(request,'index/room_search.html',{'result':result})
def search_by_category(request,category_name):
    result=Room.objects.filter(category__name=category_name)
    return render(request,'index/room_search.html',{'result':result})