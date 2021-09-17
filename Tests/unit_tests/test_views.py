"""
This file demonstrates writing tests using the unittest module.
"""

import django
from django.test import TestCase
import os
import sys

"""
When we use Django, we have to tell it which settings we are using. We do this by using an environment variable, DJANGO_SETTINGS_MODULE. 
This is set in manage.py. We need to explicitly set it for tests to work with pytest.
"""

sys.path.append(os.path.join(os.getcwd(), 'Application'))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "python_webapp_django.settings"
)
django.setup()

class ViewTest(TestCase):
    """Tests for the application views."""

    if django.VERSION:
         # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
#     def setUpClass(cls):
#         super(ViewTest, cls).setUpClass()
        def setUp(self):
            pass

    def test_unit_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        pass

    def test_unit_contact(self):
        """Tests the contact page."""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)
        pass

    def test_unit_about(self):
        """Tests the about page."""
        response = self.client.get('/about')
        self.assertEqual(response, 'About', 3, 200response.status_code, 200)
        pass
