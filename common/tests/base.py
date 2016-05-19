from django.contrib.auth.models import User
from django.test.testcases import TestCase
from django.conf import settings


class BaseTestCase(TestCase):
    """
    base test case class for common stuff and utilities 
    to be used by test cases of other modules
    """

    def setUp(self):

        # creating user
        self.username = 'neobytes'
        self.password = 'neopass'
        self.user = User.objects.create_user(self.username, 'neobytes@abcdomain.com', self.password)

