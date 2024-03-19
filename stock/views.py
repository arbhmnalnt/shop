from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import io
from barcode import EAN13
from barcode.writer import ImageWriter
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages




class StockListView(ListView):
    model = Box
    template_name = 'stock/Stock_list.html'
    context_object_name = 'boxes'
    ordering = ['-pk']

# class StockDetailView(DetailView):
#     model = Box
#     template_name = 'Stock_detail.html'

class StockCreateView(CreateView):
    model           = Box
    template_name   = 'stock/Stock_form.html'
    form_class      = BoxForm
    success_url     = reverse_lazy('stock:list')
    

class StockUpdateView(UpdateView):
    model = Box
    template_name   = 'stock/Stock_form.html'
    form_class      = BoxForm
    success_url     = reverse_lazy('stock:list')


class StockDeleteView(DeleteView):
    model = Box
    template_name = 'stock/stock_confirm_delete.html'
    success_url = reverse_lazy('stock:list')  # Replace with your list view URL

    def delete(self, request, *args, **kwargs):
        """
        Overrides the default delete method to handle deletion and message display.
        """
        self.object.delete()
        messages.success(request, 'Record deleted successfully!')  # Use success message
        return redirect(self.success_url)

def barcode_image(request, box_id):
    Stock = get_object_or_404(Box, pk=box_id)
    if Stock.barcode is not None:
        barcode_value = Stock.barcode
        ean_instance = EAN13(barcode_value, writer=ImageWriter())
        buffer = io.BytesIO()
        ean_instance.write(buffer)
        return HttpResponse(buffer.getvalue(), content_type='image/png')
    else:
        return HttpResponse("No barcode found for this Stock.", status=404)