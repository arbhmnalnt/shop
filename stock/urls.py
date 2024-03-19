from django.urls import path
from .views import *

app_name    =   'stock'

urlpatterns = [
    path('', StockListView.as_view(), name='list'),
    # path('<int:pk>/', StockDetailView.as_view(), name='Stock_detail'),
    path('new/', StockCreateView.as_view(), name='Stock_create'),
    path('<int:pk>/update/', StockUpdateView.as_view(), name='Stock_update'),
    path('<int:pk>/delete/', StockDeleteView.as_view(), name='Stock_delete'),
    path('<int:box_id>/barcode/', barcode_image, name='box_barcode'),

]