from django.contrib import admin
from logistics.models import LocationType, Location, DocumentType, Document, Shipment, ProductInShipment

admin.site.register(LocationType)
admin.site.register(Location)
admin.site.register(DocumentType)
admin.site.register(Document)
admin.site.register(Shipment)
admin.site.register(ProductInShipment)
