from django.db import models

class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Item(models.Model):
    PERISHABLE = 'perishable'
    NON_PERISHABLE = 'non_perishable'

    ITEM_TYPE_CHOICES = [
        (PERISHABLE, 'Perishable'),
        (NON_PERISHABLE, 'Non-Perishable'),
    ]

    type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=5, decimal_places=2)
    fix_price = models.DecimalField(max_digits=5, decimal_places=2)

