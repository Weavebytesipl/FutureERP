from django.contrib import admin

from common.models import Product, Customer, Staff


# registering models
admin.site.register(Customer)
admin.site.register(Staff)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'wholesale_price', 'retail_price', 'created_at')

admin.site.register(Product, ProductAdmin)
