from django.urls import path
from .views import *

app_name    =   'stock'

urlpatterns = [
    path('', StockListView.as_view(), name='list'),
    path('Stock/<int:pk>/', StockDetailView.as_view(), name='Stock_detail'),
    path('Stock/new/', StockCreateView.as_view(), name='Stock_create'),
    path('Stock/<int:pk>/update/', StockUpdateView.as_view(), name='Stock_update'),
    path('box/<int:box_id>/barcode/', barcode_image, name='box-barcode'),

]