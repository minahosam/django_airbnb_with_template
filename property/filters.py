
import django_filters
from .models import Room

class PropertyFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Room
        fields = ['title', 'price', 'location' ,'category']