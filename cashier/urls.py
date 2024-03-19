from django.urls import path
from . import views
from stock.views import barcode_image


urlpatterns = [
    path('', views.home),
    #path('box/<int:box_id>/barcode/', barcode_image, name='box-barcode'),
]