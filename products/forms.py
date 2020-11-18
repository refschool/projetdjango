from django import forms
from .models import Product
from django.forms import ModelForm


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    price = forms.FloatField()
    stock = forms.IntegerField()
    image = forms.CharField(max_length=2000)


class MyProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']  #or use tuple