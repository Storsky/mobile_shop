from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Model_id(models.Model):
    name = models.CharField(max_length=30)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    specs = models.TextField()
    image = models.ImageField(blank=True)
    description = models.TextField()

    def __str__(self):
        return '%s %s' % (self.brand, self.name)

class Phone(models.Model):
    title = models.CharField(max_length=30)
    model_id = models.ForeignKey(Model_id, on_delete = models.CASCADE)
    quantity = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2)