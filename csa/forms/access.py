from registration.forms import RegistrationForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class RegistrationForm(RegistrationForm):
    first_name = forms.CharField(label='Όνομα')
    last_name = forms.CharField(label='Επώνυμο')
    phone_number = PhoneNumberField(
        label='Τηλέφωνο',
        widget=PhoneNumberInternationalFallbackWidget)
