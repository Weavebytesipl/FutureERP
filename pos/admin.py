from django.contrib import admin

from pos.models import ProductInTransaction, Payment, PaymentMethod, Transaction, SalesOutlet

admin.site.register(SalesOutlet)
admin.site.register(ProductInTransaction)
admin.site.register(PaymentMethod)
admin.site.register(Transaction)

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('method', 'transaction', 'amount', 'other_details')

admin.site.register(Payment, PaymentAdmin)

