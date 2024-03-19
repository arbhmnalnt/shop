from django import forms
from .models import Box

class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ['name', 'price', 'amount']  # Exclude 'barcode' field as it's generated automatically
    
    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation if needed
        return cleaned_data