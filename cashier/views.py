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


class SoldListView(ListView):
    model = Sold
    template_name = 'cashier/sold_list.html'
    context_object_name = 'solds'
    ordering = ['-pk']

class SoldCreateView(CreateView):
    model           = Sold
    template_name   = 'cashier/sold_form.html'
    form_class      = SoldForm
    success_url     = reverse_lazy('cashier:list')
