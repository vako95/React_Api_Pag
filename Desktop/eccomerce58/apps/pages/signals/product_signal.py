
from django.db.models.signals import pre_save
from ..models import Product, ProductTrash

def product_signal(instance, *args, **kwargs):
    pass
