from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import m2m_changed


class CartManger(models.Manager):
    def new_or_create_cart(self,request):
        cartid = request.session.get("cart_id", None)
        q = self.get_queryset().filter(id=cartid)
        if q.count() == 1 and request.user.is_authenticated:
            cart_object = q.first()
            if cart_object.user is None:
                cart_object.user = request.user
                cart_object.save()
        else:
            cart_object = self.create(user=request.user)
            request.session['cart_id'] = cart_object.id
            cart_object.user = request.user
            cart_object.save()
        return cart_object

class cart(models.Model):
    user     = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    Products = models.ManyToManyField(Product, blank=True)
    total    = models.DecimalField(default= 0.00, max_digits=100, decimal_places=2)
    objects  = CartManger()

    def __str__(self):
        return str(self.id)

def m2m_cart(sender, instance, action, *args, **kwargs):
    total = 0
    for x in instance.Products.all():
        total = total + x.price
        instance.total = total
        instance.save()

m2m_changed.connect(m2m_cart,sender=cart.Products.through)
