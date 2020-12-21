from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post, category
from taggit.models import Tag
from django.db.models import Count, Q
class blog_list(ListView):
    model=Post
    paginate_by=3
    def get_queryset(self):
        n=self.request.GET.get('q','')
        object_list=Post.objects.filter(Q(title__icontains=n)|Q(description__icontains=n))
        return object_list
    
class blog_detail(DetailView):
    model=Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_categories"] = category.objects.all().annotate(post_count=Count('room_category'))
        context['all_posts']=Post.objects.all()[:2]
        context['all_tags']=Tag.objects.all()
        return context
    