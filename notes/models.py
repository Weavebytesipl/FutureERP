from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    category for a note
    """
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)

    def __unicode__(self):
        """
        function returns unicode representation of a category
        """
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Note(models.Model):
    """
    model for a note
    """
    title = models.CharField(max_length=64)
    details = models.TextField()
    category = models.ForeignKey(Category)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """
        function returns unicode representation of a note
        """
        return self.title
