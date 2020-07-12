from django import forms
from .models import Pledge

class PledgeForm(forms.ModelForm):
    class Meta:
        model = Pledge
        fields = [
            'first_name',
            'last_name',
            'email',
            'amount'
        ]
