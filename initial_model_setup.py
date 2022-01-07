from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

# Create superuser
try:
    User.objects.get(username='admin')
except User.DoesNotExist:
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')

# OAtuh django-allauth setup.
site, site_created = Site.objects.get_or_create(domain='127.0.0.1:8000', name='127.0.0.1:8000')
social_app, social_app_created = SocialApp.objects.get_or_create(provider='google', name='oauth-iban-app',
                                      client_id='<client_id>', 
                                      secret='<secret>')
if social_app_created:
    social_app.sites.set([site])
