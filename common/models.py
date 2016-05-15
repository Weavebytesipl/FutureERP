from __future__ import unicode_literals

from django.db import models


class Product(models.Model):
    """
    product model for the items etc.
    """
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, unique=True)
    wholesale_price = models.PositiveIntegerField(default=0)
    retail_price = models.PositiveIntegerField(default=0)
    img = models.ImageField(upload_to = 'prod_imgs/', default = 'prod_imgs/default.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """
        function returns unicode representation of a product
        """
        return self.name
