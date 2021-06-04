from celery import shared_task
from django.core.mail import message, send_mail
from orders.models import Order

@shared_task
def order_created(order_id):
    """
    task to send an email when an order is successfully created 
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name}, \n\n' \
        f'You have successfully placed your order.' \
        f'Your order ID is {order.id}.'

    mail_sent = send_mail(subject, message, 'admin@agribizz.com', [order.email])

    return mail_sent