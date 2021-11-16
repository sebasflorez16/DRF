from django.urls import path
from apps.products.api.views.general_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveUpdateDeleteAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit' ),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator' ),
    path('category_product/', CategoryProductListAPIView.as_view(), name='category_product' ),
    path('product/', ProductListCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve-update-destroy/<int:pk>/', ProductRetrieveUpdateDeleteAPIView.as_view(), name='product_retrieve_update_destroy'),
    #path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),Fueron reemplazadas en la vista por el mixin de las CRUD casi completo
    #path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),

]