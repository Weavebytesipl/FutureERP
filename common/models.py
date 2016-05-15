from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class SingletonModel(models.Model):
    """
    Singleton Django Model

    Ensures there's always only one entry in the database, and can fix the
    table (by deleting extra entries) even if added via another mechanism.

    Also has a static load() method which always returns the object - from
    the database if possible, or a new empty (default) instance if the
    database is still empty. If your instance has sane defaults (recommended),
    you can use it immediately without worrying if it was saved to the
    database or not.

    Useful for things like system-wide user-editable settings.

    Thanks to this link:-
    https://gist.github.com/senko/5028413
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Save object to the database. Removes all other entries if there
        are any.
        """
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        """
        Load object from the database. Failing that, create a new empty
        (default) instance of the object and return it (without saving it
        to the database).
        """

        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


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


class Customer(models.Model):
    """
    customer model for the various module of future erp
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
        """
        function returns unicode representation of a product
        """
        return "%s" % self.user


class Staff(models.Model):
    """
    staff model for the various module of future erp
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
        """
        function returns unicode representation of a product
        """
        return "%s" % self.user

    class Meta:
        verbose_name_plural = "staff"
