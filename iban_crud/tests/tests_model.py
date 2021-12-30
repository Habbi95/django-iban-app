from django.test import TestCase

from iban_crud.models import IBANUser
from django.contrib.auth.models import User

class IBANUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='Javier')
        IBANUser.objects.create(first_name='Javier', last_name='Vargas', iban='ES8121003943748883455558', created_by=user)

    def test_first_name_max_length(self):
        iban_user = IBANUser.objects.get(id=1)
        max_length = iban_user._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_last_name_max_length(self):
        iban_user = IBANUser.objects.get(id=1)
        max_length = iban_user._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_iban_max_length(self):
        iban_user = IBANUser.objects.get(id=1)
        max_length = iban_user._meta.get_field('iban').max_length
        self.assertEqual(max_length, 34)

    def test_str_object_format(self):
        iban_user = IBANUser.objects.get(id=1)
        expected_object_name = f'{iban_user.first_name} {iban_user.last_name} IBAN: {iban_user.iban}'
        self.assertEqual(str(iban_user), expected_object_name)