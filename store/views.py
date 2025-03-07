from django.shortcuts import render, redirect
from .models import products
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from shopingCart.shopingcart import ShoppingCart
from orders.models import orders, allOrders
from django.utils.html import strip_tags

def store_view(request):
    products_all = products.objects.all()
    return render(request, 'store.html', {'products_all': products_all})

def send_order_email(**kwargs):
    topic = 'Thanks for the order!'
    message_ = render_to_string('emails/order.html', {
        'orders': kwargs.get('order'),
        'lines_orders': kwargs.get('lines_orders'),
        'user_name': kwargs.get('user_name'),
        'emailUser': kwargs.get('emailUser'),
    })
    message_text = strip_tags(message_)
    from_email = 'appwebmail2025@gmail.com'
    to = kwargs.get('emailUser')
    send_mail(topic, message_text, from_email, [to], html_message=message_)

@login_required(login_url='/auth')
def buy_everything(request):
    # Crear el pedido en la base de datos
    orders_all = orders.objects.create(user=request.user)
    shopp_cart = ShoppingCart(request)
    lines_orders = []
    for key, value in shopp_cart.shopping.items():
        product_instance = products.objects.get(pk=key)
        lines_orders.append(allOrders(
            product_id=product_instance,
            amount=value['amount'],
            user=request.user,
            order_id=orders_all
        ))
    allOrders.objects.bulk_create(lines_orders)
    send_order_email(
        order=orders_all,
        lines_orders=lines_orders,
        user_name=request.user.username,
        emailUser=request.user.email
    )
    messages.success(request, 'Nice! Your order is complete')
    return redirect('home')
