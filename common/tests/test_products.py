from .base import BaseTestCase
from common.models import Product

class ProductTestCase(BaseTestCase):
    def setUp(self):
        """
        create a test product test cases
        """

        super(ProductTestCase, self).setUp()

        # creating dummy product
        self.product = Product()
        self.product.name = "Table"
        self.product.description = 'Wooden table for future erp workers'
        self.product.wholesale_price = 1200
        self.product.retail_price = 1500
        self.product.save()

    def test_product_was_added(self):
        """
        ensure that product was added
        """
        table = Product.objects.get(name="Table")
        self.assertEqual(self.product.name, table.name)


    def test_edit_product_name(self):
        """
        ensure that product name can be edited
        """
        new_name = "New Table"
        self.product.name = new_name
        self.product.save()

        # esuring that product was edited
        table = Product.objects.get(name=new_name)
        self.assertEqual(self.product.name, table.name)

    def tearDown(self):
        """
        cleanup saved/dummy data etc
        """
        if self.product:
            self.product.delete()
        if self.user:
            self.user.delete()
