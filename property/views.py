from django.shortcuts import render
from . import models
from django.views.generic import ListView , DetailView
class roomlist(ListView):
    model=models.Room
class roomdetail(DetailView):
    model=models.Room