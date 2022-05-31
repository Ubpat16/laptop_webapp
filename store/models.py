from django.conf import settings
from django.db import models

# choices
from django.urls import reverse

CPU_TYPE = (
    ('i3', 'Intel Core i3'),
    ('i5', 'Intel Core i5'),
    ('i7', 'Intel Core i7'),
    ('i9', 'Intel Core i9'),
    ('Duos', 'Intel Core Duos'),
    ('Cel', 'Intel Celeron'),
    ('Cen', 'Intel Centrino'),
    ('AMD', 'AMD CPU')
)

RAM = (
    (1, '1GB'),
    (2, '2GB'),
    (4, '4GB'),
    (6, '6GB'),
    (8, '8GB'),
    (16, '16GB'),
    (32, '32GB'),
)

CPU_GEN = (
    ('1st', 'First Gen'),
    ('2nd', 'Second Gen'),
    ('3rd', 'Third Gen'),
    ('4th', 'Forth Gen'),
    ('5th', 'Fifth Gen'),
    ('6th', 'Sixth Gen'),
    ('7th', 'Seventh Gen'),
    ('8th', 'Eighth Gen'),
    ('9th', 'Ninth Gen'),
    ('10th', 'Tenth Gen')
)

STORAGE_TYPE = (
    ('HDD', 'Hard Disk Drive'),
    ('SSD', 'Solid State Drive'),
    ('SSHD', 'SS + HD Drive'),
)


# Create your models here.

class Laptop(models.Model):
    brand_name = models.CharField(max_length=25)
    brand_model = models.CharField(max_length=25)
    cpu_type = models.CharField(max_length=25, choices=CPU_TYPE)
    cpu_gen = models.CharField(max_length=25, choices=CPU_GEN)
    ram = models.IntegerField(choices=RAM)
    storage = models.CharField(max_length=15, choices=STORAGE_TYPE)
    photo = models.ImageField(upload_to='media')
    price = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.brand_name} {self.brand_model}'

    def get_absolute_url(self):
        return reverse("store:product", kwargs={
            "pk": self.pk
        })

    def get_add_to_cart_url(self):
        return reverse("store:product", kwargs={
            "pk": self.pk
        })

    def get_remove_fron_cart__url(self):
        return reverse("store:product", kwargs={
            "pk": self.pk
        })


class OrderItem(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.items}"


class Order(models.Model):
    order_no = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    order_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order: {self.order_no}"
