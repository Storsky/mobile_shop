from django.db import models
from users.models import Profile

COLORS_OF_PHONES_CHOICES = [
    ('R', 'Red'),
    ('B', 'Black'),
    ('BL', 'Blue'),
    ('Y', 'Yellow'),
    ('GR', 'Green'),
    ('G', 'Gray'),
]


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    specs = models.TextField()
    image = models.ImageField(blank=True, upload_to='static/phones/img')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=2,
                    choices = COLORS_OF_PHONES_CHOICES,
                    default = 'B')
    profiles = models.ManyToManyField(Profile, through='ProfileProduct', related_name = 'products')
    def __str__(self):
        return '%s %s' % (self.brand, self.name)


class ProfileProduct(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name = 'ProfileProduct')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = 'ProfileProduct')
    created_at = models.DateTimeField(auto_now_add=True)


class PhoneReview(models.Model):
    phone = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return '%s %s' % (self.phone.name, self.user)