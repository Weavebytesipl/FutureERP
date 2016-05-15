from __future__ import unicode_literals

from django.db import models
from common.models import SingletonModel


class Preference(SingletonModel):
    """
    A singleton model with only 1 row in data for 
    storing user preferences
    """

    website_title = models.CharField(max_length=128)
    enable_logistics = models.BooleanField(default=True)
    enable_point_of_sale = models.BooleanField(default=True)
    enable_retail = models.BooleanField(default=True)
    enable_notes = models.BooleanField(default=True)

    def __unicode__(self):
        """
        function returns unicode representation of a preferences
        """
        return "%s Preferences" % self.website_title
