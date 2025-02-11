from django.db import models

class Product(models.Model):
    description = models.CharField(max_length=45)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def order_new(data):
    product_id = int(data['product_id'])
    quantity = int(data['quantity'])
    product = Product.objects.get(id=product_id)
    unit_price = product.price
    return Order.objects.create(
        quantity_ordered = quantity,
        total_price = quantity * unit_price
    )

def get_all_products():
    return Product.objects.all()

def get_order_by_id(id):
    return Order.objects.get(id=id)