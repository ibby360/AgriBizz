from django import forms
from orders.models import Order


class OrderCreateForm(forms.ModelForm):


        class Meta:
                model = Order
                fields = ['first_name', 'last_name', 'email',
                'address', 'address2', 'city', 'order_notes']

                widgets = {
                        'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
                        'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
                        'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
                        'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '123 Main Street'}),
                        'address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, Studio or Floor'}),
                        'city': forms.Select(attrs={'class': 'form-control',}),
                        'order_notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Note on your order, e.g. special notes concering derivery'}),
                }
