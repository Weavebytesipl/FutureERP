from __future__ import unicode_literals

from django.db import models
from common.models import Customer
from common.models import Staff
from common.models import Product
from django.utils.translation import ugettext_lazy as _


class SalesOutlet(models.Model):
	"""
	model for sales outlet details
	"""
	title = models.CharField(max_length=128, verbose_name=_('Outlet Name'))
	details = models.CharField(max_length=1024, verbose_name=_('Sales Outlet Details'))
	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

	def __unicode__(self):
		"""
		function returns unicode representation of sales outlet name
		"""
		return "%s" % self.title


class Transaction(models.Model):
	"""
	model for transactions
	"""
	customer = models.ForeignKey(Customer)	
	staff = models.ForeignKey(Staff)
	
	# time stamps !
	created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

	wholesale_price = models.CharField(max_length=128, verbose_name=_('Wholesale Price'))	
	retail_price = models.CharField(max_length=128, verbose_name=_('Retail Price'))
	other_details = models.CharField(max_length=1024, verbose_name=_('Other Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of 
		"""
		return "%s" % self.customer


class PaymentMethod(models.Model):
	"""
	model for payment method
	"""
	name = models.CharField(max_length=128, verbose_name=_('Payment Method Name'))	
	description = models.CharField(max_length=128, verbose_name=_('Payment Desciption'))

	def __unicode__(self):
		"""
		function returns unicode representation of 
		"""
		return "%s" % self.name


class Payment(models.Model):
	"""
	model for payment 
	"""
	method = models.ForeignKey(PaymentMethod)
	transaction = models.ForeignKey(Transaction)
	amount = models.PositiveIntegerField(_('Payment Amount'), default=0, null=True, blank=True)
	other_details = models.CharField(max_length=1024, verbose_name=_('Other Details'))

	def __unicode__(self):
		"""
		function returns unicode representation of payment 
		"""
		return "%d" % self.method


class ProductInTransaction(models.Model):
	"""
	model for product in transaction
	"""
	product = models.ForeignKey(Product)
	transaction = models.ForeignKey(Transaction)
	quantity = models.PositiveIntegerField(_('Quantity'), default=0, null=True, blank=True)	

	def __unicode__(self):
		"""
		function returns unicode representation of product in transaction
		"""
		return "%d" % self.product_id















