from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from django.core.validators import MaxValueValidator, MinValueValidator
from .category import Category
from .brand import  Brand

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Title",
        help_text="Enter the product name (max 255 characters)."
    )
    # slug = models.SlugField(
    #     max_length=255,
    #     unique=True,
    #     null=False,
    #     blank=True,
    #     verbose_name="Slug",
    #     help_text="Automatically generated based on the Title."

    # )
    # content = models.TextField(
    #     null=False,
    #     blank=True,
    #     verbose_name="Content",
    #     help_text="Content about product"
    # )
    # image = models.ImageField(
    #     upload_to="product/%Y/%m/%d/",
    #     null=True,
    #     blank=True,
    #     verbose_name="Image",
    #     help_text="Upload the Product Image."
    # )
    # price = models.DecimalField(
    #     max_digits=5,
    #     decimal_places=2,
    #     validators=[MaxValueValidator(100), MinValueValidator(1)],
    #     null=True,
    #     blank=True,
    #     verbose_name="Price",
    #     help_text="Product price",
    #     default=0,
    # )
    # discount = models.DecimalField(
    #     max_digits=4,
    #     decimal_places=1,
    #     validators=[MaxValueValidator(100), MinValueValidator(0)],
    #     blank=True,
    #     default=0,
    #     verbose_name="Disocunt(%)",
    #     help_text="Enter a discount percentage (0 to 100).",
    # )
    # status = models.BooleanField(
    #     default=True,
    #     verbose_name="Status",
    #     help_text="Check this box if the item is active. Uncheck to disable."
    # )
    # brand = models.ForeignKey(
    #     Brand,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     related_name="products",
    #     verbose_name="Brand",
    #     help_text="Select a brand for the product.",
    # )
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     related_name="products",
    #     verbose_name="Category",
    #     help_text="Select a Category for the product.",
    # )
    # time_create = models.DateTimeField(
    #     auto_now_add=True,
    #     verbose_name="Create time",
    #     help_text="Time when the item was created.",
    # )
    # time_update = models.DateTimeField(
    #     auto_now=True,
    #     verbose_name="Update at",
    #     help_text="time when the item was update.",
    # )
    time_deleted = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Deleted At",
        help_text="Date and time when the object was deleted.",
    )
 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pixel:product_detail", kwargs={"slug":self.slug})
    
    def delete(self, is_hard_delete=False):
        if is_hard_delete:
            super().delete()
        else:    
            self.time_deleted = now()
            self.save()
    

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"
        # ordering = ("-time_create",)

        


class ProductTrash(Product):

    def delete(self):
        self.time_deleted = None
        self.save()


      
    
    class Meta:
        verbose_name = "Selected All"
        verbose_name_plural = "Product Trash"
        proxy = True

    





    

    

       

    
        

