from rest_framework import viewsets
from .models import Property
from .serializers import PropertySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, CharFilter

class PropertyFilter(FilterSet):
    facilities = CharFilter(method='filter_facilities')

    class Meta:
        model = Property
        fields = []

    def filter_facilities(self, queryset, name, value):
        return queryset.filter(facilities__icontains=value)

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter
