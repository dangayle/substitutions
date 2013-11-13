from django.test import TestCase
from substitutions.templatetags.substitutions import substitute


class TestSubstitution(TestCase):
    def test_title_text(self):
        title_text = substitute("Inside Elon Musk's new electric car").upper()
        self.assertEqual(title_text, "INSIDE ELON MUSK'S NEW ATOMIC CAT")
