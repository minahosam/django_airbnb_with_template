from django.shortcuts import get_object_or_404, redirect, render
from .models import Profile
from .forms import UserForm , ProfileForm , UserCreateForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from property.models import Room, RoomBook
from property.forms import roomreviewform
# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def profile(request):
    profile = Profile.objects.get(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })


def user_reservation(request):
    my_reservation = RoomBook.objects.filter(name=request.user)
    return render(request,'profile/my_reservation.html',{'my_reservation':my_reservation})
def rate_feedback(request,slug):
    room=get_object_or_404(Room,slug=slug)
    if request.method=='POST':
        form =roomreviewform(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.room=room
            myform.author=request.user
            myform.save()
            return redirect('rooms:list')
    else:
        form=roomreviewform()
    return render(request,'profile/feedback.html',{'form':form})
def show_my_listing(request):
    listing=Room.objects.filter(owner=request.user)
    return render(request,'profile/listing.html',{'listing':listing})











