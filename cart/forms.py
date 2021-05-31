from django import forms
from django.forms import widgets

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProdcutForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, widget=forms.Select(attrs={'class': 'custom-select my-1'}))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

