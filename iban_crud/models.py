from django.db import models
from django.contrib.auth.models import User
from localflavor.generic.models import IBANField

# Create your models here.
class IBANUser(models.Model):
    # Django admin users will be considered as app "administrators". IBAN users will be users added by administrators
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    iban = IBANField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} IBAN:  {str(self.iban)}'