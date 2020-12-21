from django.forms import forms
from property.models import category
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.edit import FormMixin
from . import models
from django.views.generic import ListView , DetailView
from .filters import PropertyFilter
from .forms import BookForm
from django_filters.views import FilterView
class roomlist(FilterView):
    model=models.Room
    filterset_class=PropertyFilter
    template_name='property/room_list.html'
class roomdetail(FormMixin,DetailView):
    model=models.Room
    form_class=BookForm
    success_url='/rooms/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related_room"] = models.Room.objects.filter(category=self.get_object().category)
        return context
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.room=self.object
            my_form.save()
        return redirect('rooms:list')