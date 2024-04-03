from django.urls import path
from .views import *

app_name    =   'cashier'

urlpatterns = [
    path('', SoldListView.as_view(), name='list'),
    # path('<int:pk>/', SoldDetailView.as_view(), name='Sold_detail'),
    path('new/', SoldCreateView.as_view(), name='Sold_create'),
    # path('<int:pk>/update/', SoldUpdateView.as_view(), name='Sold_update'),
    # path('<int:pk>/delete/', SoldDeleteView.as_view(), name='Sold_delete'),
]