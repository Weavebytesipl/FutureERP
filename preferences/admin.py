from django.contrib import admin

from preferences.models import Preference


class PreferenceAdmin(admin.ModelAdmin):
    list_display = ('website_title', 'enable_logistics', 'enable_notes')

# registering models
admin.site.register(Preference, PreferenceAdmin)
