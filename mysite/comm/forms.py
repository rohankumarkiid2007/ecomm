from django import forms
from django.forms import fields
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','description','price','picture']