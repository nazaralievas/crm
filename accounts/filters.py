import django_filters
from django_filters import DateFilter
# from django_filters import CharFilter

from .models import Order


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte')
    # если бы нужна была функция поиска по словам (если бы было поле note в модели Order)
    # note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = ['product', 'status']

