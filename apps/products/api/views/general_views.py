from rest_framework import generics

from apps.base.api import GeneralListAPIView
from apps.products.api.serializers.general_serializers import MeasureUniteSerializer, CategoryProductSerializer, InidicatorSerializer


class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUniteSerializer


class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = InidicatorSerializer

    """def get_queryset(self):
        return Indicator.objects.filter(state = True)"""


class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
