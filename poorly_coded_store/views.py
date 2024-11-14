from django.shortcuts import render, redirect
from . import models

def index(request):
    context = {
        "all_products": models.get_all_products()
    }
    if 'total' not in request.session:
        request.session['total'] = 0
    return render(request, "store/index.html", context)

def checkout(request):
    order = models.order_new(request.POST)
    id = str(order.id)
    print("Charging credit card...")
    if 'total' in request.session:
        request.session['total'] += float(order.total_price)
    return redirect('/amadon/checkout/' + id)

def viewCheckout(request, id):
    context = {
        'order' : models.get_order_by_id(id)
    }
    return render(request, "store/checkout.html", context)