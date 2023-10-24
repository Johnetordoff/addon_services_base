from django.test import TestCase
from .factories import UserFactory


class TestTestCase(TestCase):
    def test_tests(self):
        """Simple base test to test test infrastructure"""
        pass

    def test_model(self):
        """Simple base test to test test models"""
        user = UserFactory(username="Jalen Hurts")
        user.save()
        assert user.username == "Jalen Hurts"
