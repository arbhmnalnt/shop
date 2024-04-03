from django.db import models
from stock.models import *

class Sold(TimeStampMixin, models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE,verbose_name="التصنيف")

    def __str__(self):
        self.box.name + ' : ' +str(self.box.price)