from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, 'You do not have anything in your bag at the moment!')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OxB0l05Rso9kAP54DQ5zF7W7JVAuF6QIkbKhqIfP9Hxc8tAWDI6s4INybV3hDo6FIgn0M6rOpGfD2Gb5aKZSDBd00DhDrRjhq',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
