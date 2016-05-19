from django.contrib import admin
from helpdesk.models import Complaint, Supporter

# Register your models here.

admin.site.register(Complaint)
admin.site.register(Supporter)
