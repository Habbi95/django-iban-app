from django import forms
from localflavor.generic.forms import IBANFormField

class IBANUserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last name', max_length=50)
    iban = IBANFormField(label='IBAN')