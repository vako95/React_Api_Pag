from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text="Enter the name of the product.",
        )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=False,
        blank=True,
        verbose_name="Slug",
        help_text= "Automatically generated based on the Name.",
    )
    image = models.ImageField(
        upload_to="category/%Y/%m/%d/",
        verbose_name="Image",
        null=True,
        blank=True,
        help_text="Upload the category Image."
        )
    status = models.BooleanField(
        default=True, 
        verbose_name="Status",
        help_text="Check this box if the item is active. Uncheck to disable.",
    )
    time_create = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Create at",
        help_text="Time when the item was created.",
        )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="Update at",
        help_text="time when the item was update.",
    )
    time_deleted = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Deleted At",
        help_text="Date and time when the object was deleted.",
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("categories_detail", kwargs={"slug":self.slug})
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("-time_create",)
    
    

