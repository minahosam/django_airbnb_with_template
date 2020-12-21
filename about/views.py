from about.models import faq
from django.shortcuts import render
from django.views.generic import ListView
from .models import faq,About
class about_view(ListView):
    model=faq
    fields='__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.last()
        return context
    