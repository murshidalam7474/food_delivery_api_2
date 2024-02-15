# delivery/admin.py

from django.contrib import admin
from .models import Organization, Item, Pricing

admin.site.register(Organization)
admin.site.register(Item)
admin.site.register(Pricing)
