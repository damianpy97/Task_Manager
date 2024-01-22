import django_filters
from django_filters import *
from django_filters.widgets import *
from .models import *
from django.forms import DateTimeInput


class TaskFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains', label='Name')
    note = CharFilter(field_name='description', lookup_expr='contains', label='Description')

    class Meta:
        model = Task
        fields = ['user', 'status',  'id']


class HistoryFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='contains', label='Name')
    note = CharFilter(field_name='description', lookup_expr='contains', label='Description')
    data = DateTimeFromToRangeFilter(field_name='history_date', label='Date range (YYYY-MM-DD HH:MM:SS)')
    id = AllValuesFilter(field_name='id')
    status = AllValuesFilter(field_name='status')

    TYPE_CHOICES = (
    ('+', 'added'),
    ('~', 'updated'),
    ('-', 'deleted'))
    type = ChoiceFilter(field_name='history_type', choices=TYPE_CHOICES, label='Operation type')

    class Meta:
        model = History
        fields = ['user']