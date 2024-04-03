from django.db import models
import barcode
from barcode.writer import ImageWriter

class TimeStampMixin(models.Model):
    created_at      = models.DateTimeField(auto_now_add=True,null=True)
    updated_at      = models.DateTimeField(auto_now=True,null=True)
    is_deleted      = models.BooleanField(default=False, null=True)

import random
class Box(models.Model):
    name    = models.CharField(max_length=50, null=True, blank=True, verbose_name="اسم للكرتونة")
    price   = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True,verbose_name="السعر")
    amount  = models.PositiveIntegerField( null=True, blank=True,verbose_name="عدد المنتجات")
    barcode = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="الباركود")

    def __str__(self):
        return self.name + ' : ' + str(self.price) + ' جنيه'
    
    def save(self, *args, **kwargs):
        if not self.barcode:
            self.barcode = self.generate_barcode()
        super().save(*args, **kwargs)

    def generate_barcode(self):
        unique_numbers = random.randint(100000,900000)
        barcode_value = '909102'  # You can customize prefix if needed
        # Generate barcode value here, for example, using the box ID
        # For simplicity, using the box ID as the barcode value
        barcode_value += str(unique_numbers)
        return barcode_value