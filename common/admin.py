from django.contrib import admin

from common.models import Product, Customer, Staff


# registering models
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Staff)
