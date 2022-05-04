from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify  # new
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class Product(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    title = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/', null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='True')
    detail = RichTextField(default="")  # for detail page

    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    discount_percentage = models.IntegerField(default=0)
    discount_price = models.DecimalField(max_digits=12, decimal_places=2, default=0, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'slug': self.slug})

    def get_discount_percentage(self):
        return f'-{self.discount_percentage}%'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if self.discount_percentage > 1:
            self.discount_price = float((self.discount_percentage / 100)) * float(self.price)
            super(Product, self).save(*args, **kwargs)

        super(Product, self).save(*args, **kwargs)


class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tx_ref = models.CharField(max_length=8, editable=False, default=get_random_string(8))
    full_name = models.CharField(max_length=100)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    total = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name
