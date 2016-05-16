from django.contrib import admin

from pos.models import ProductInTransaction, Payment, PaymentMethod, Transaction, SalesOutlet

admin.site.register(SalesOutlet)
admin.site.register(ProductInTransaction)
admin.site.register(Payment)
admin.site.register(PaymentMethod)
admin.site.register(Transaction)

