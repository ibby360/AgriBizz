from django.db import models
from shop.models import Product
# Create your models here.
class Order(models.Model):
    CHOICES = (
        ('Arusha', 'Arusha'),
        ('Dar es Salaam', 'Dar es Salaam'),
        ('Geita', 'Geita'),
        ('Kagera', 'Kagera'),
        ('Mwanza', 'Mwanza'),
        ('Morogoro', 'Morogoro'),
        ('Shinyanga', 'Shinyanga'),
        ('Tabora', 'Tabora'),
        ('Singida', 'Singida'),
        ('Simiyu', 'Simiyu'),
        ('Mbeya', 'Mbeya'),
        ('Mara', 'Mara'),
        ('Kilimanjaro', 'Kilimanjaro'),
        ('Tanga', 'Tanga'),
        ('Kigoma', 'Kigoma'),
        ('Mtwara', 'Mtwara'),
        ('Pwani', 'Pwani'),
        ('Simiyu', 'Simiyu'),
        ('Songwe', 'Songwe'),
        ('Lindi', 'Lindi'),
        ('Dodoma', 'Dodoma'),
        ('Singida', 'Singida'),
        ('Ruvuma', 'Ruvuma'),
        ('Njombe', 'Njombe'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    city = models.CharField(max_length=150, choices=CHOICES)
    order_notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity