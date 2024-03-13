from django.shortcuts import render
from django.http import HttpResponse
import io
from barcode import EAN13
from barcode.writer import ImageWriter
from django.shortcuts import get_object_or_404
from .models import Box


def home(request):
    return render(request, 'stock\index.html')


def barcode_image(request, box_id):
    box = get_object_or_404(Box, pk=box_id)
    if box.barcode is not None:
        barcode_value = box.barcode
        ean_instance = EAN13(barcode_value, writer=ImageWriter())
        buffer = io.BytesIO()
        ean_instance.write(buffer)
        return HttpResponse(buffer.getvalue(), content_type='image/png')
    else:
        return HttpResponse("No barcode found for this box.", status=404)