from django.forms import ModelForm
from .models import CreditCard


class CreditCardForm(ModelForm):
    class Meta:
        model = CreditCard
        fields = ['number', 'expiry', 'cvv']
