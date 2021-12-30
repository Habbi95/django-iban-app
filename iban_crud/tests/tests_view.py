from django.test import TestCase

from iban_crud.models import IBANUser
from django.contrib.auth import get_user_model
from django.urls import reverse

class IBANUserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        user1 = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        user2 = User.objects.create_user('temporary2', 'temporary@gmail.com', 'temporary')

        IBANUser.objects.create(first_name='Javier', last_name='Vargas', iban='ES8121003943748883455558', created_by=user1)
        IBANUser.objects.create(first_name='Pepe', last_name='Rindus', iban='ES8121003943748883455558', created_by=user2)
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('get_users'))
        self.assertRedirects(response, '/accounts/login/?next=/crud/get_users') # Redirects to login page
    
    def test_logged_in_uses_correct_template(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('get_users'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'temporary')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'get_users.html')

    def test_user_cannot_see_other_objects(self):
        user1_object_id = IBANUser.objects.get(first_name='Javier').id
        user2_object_id = IBANUser.objects.get(first_name='Pepe').id

        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('modify_user', kwargs={'user_id': user2_object_id}))
        self.assertEqual(response.status_code, 404)

        self.client.login(username='temporary2', password='temporary')
        response = self.client.get(reverse('modify_user', kwargs={'user_id': user1_object_id}))
        self.assertEqual(response.status_code, 404)

        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('modify_user', kwargs={'user_id': user1_object_id}))
        self.assertEqual(response.status_code, 200)