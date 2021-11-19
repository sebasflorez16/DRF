from rest_framework import generics

from rest_framework import viewsets

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUniteSerializer, CategoryProductSerializer, InidicatorSerializer


class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUniteSerializer


class IndicatorViewSet(viewsets.ModelViewSet):
    serializer_class = InidicatorSerializer

    """def get_queryset(self):
        return Indicator.objects.filter(state = True)"""


class CategoryProductViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
