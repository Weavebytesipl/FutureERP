from django.contrib import admin

from notes.models import Category, Note


# registering models
admin.site.register(Category)
admin.site.register(Note)
