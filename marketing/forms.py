from django.db.models.base import Model
from django import forms
from django.db.models.fields import TextField
from django.forms import ModelForm
from django.forms.widgets import NumberInput, Select
from marketing.models import PostProduct


class SellProduct(forms.ModelForm):
    class Meta:
        model = PostProduct
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone.. e.g 0717000011'}),
            'region': forms.Select(attrs={'class': 'form-control', 'placeholder': '--SELECT--'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your District'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Ward'}),


            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'scale': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),


        }
