from django import forms
from .models import Sold

class SoldForm(forms.ModelForm):
    class Meta:
        model = Sold
        fields = ['box']
    
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation if needed
        return cleaned_data