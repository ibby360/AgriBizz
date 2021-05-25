from django.db.models.base import Model
from django import forms
from django.db.models.fields import TextField
from django.forms import ModelForm
from django.forms.widgets import NumberInput, Select
from marketing.models import PostProduct
from phonenumber_field.modelfields import PhoneNumberField


class SellProduct(forms.ModelForm):
    class Meta:
        model = PostProduct
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Fist Name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Middle Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone.. e.g +255700000017'}),
            'region': forms.Select(attrs={'class': 'form-control', 'placeholder': '--SELECT--'}),
            'district': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your District'}),
            'ward': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Ward'}),


            'product_name': forms.Select(attrs={'class': 'form-control'}),
            'unit': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}),


        }
