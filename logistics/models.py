from __future__ import unicode_literals

from django.db import models
from common.models import Customer, Product
from django.utils.translation import ugettext_lazy as _


class LocationType(models.Model):
	"""
	model for location type
	"""
	type = models.CharField(max_length=128, verbose_name=_('Location Type'))

	def __unicode__(self):
		"""
		function returns unicode representation of location type
		"""
		return "%s" % self.type


class Location(models.Model):
	"""
	model for location
	"""
	name = models.CharField(max_length=128, verbose_name=_('Location Name'))
	type = models.ForeignKey(LocationType)
	details = models.CharField(max_length=1024, verbose_name=_('Location Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of location type
		"""
		return "%s" % self.name


class DocumentType(models.Model):
	"""
	model for document type
	"""
	name = models.CharField(max_length=128, verbose_name=_('Document Name'))
	details = models.CharField(max_length=1024, verbose_name=_('Location Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of document type
		"""
		return "%s" % self.name


class Document(models.Model):
	"""
	model for document
	"""	
	name = models.ForeignKey(DocumentType)
	details = models.CharField(max_length=1024, verbose_name=_('Other Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of document 
		"""
		return "%s" % self.name


class Shipment(models.Model):
	"""
	model for shipment
	"""
	name = models.ForeignKey(Customer)
	from_location_name = models.ForeignKey(Location, related_name='from_location')
	document_name = models.ForeignKey(Document)
	to_location_name = models.ForeignKey(Location, related_name='to_location')
	details = models.CharField(max_length=1024, verbose_name=_('Other Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of Shipment
		"""
		return "%s" % self.name


class ProductInShipment(models.Model):
	"""
	model for product in ProductInShipment
	"""
	name = models.ForeignKey(Product)
	shipment_name = models.ForeignKey(Shipment)
	quantity = models.PositiveIntegerField(_('Quantity'), default=0, null=True, blank=True)
	cost = models.PositiveIntegerField(_('Cost'), default=0, null=True, blank=True)

	def __unicode__(self):
		"""
		function returns unicode representation of product in shipment
		"""
		return "%s" % self.name


