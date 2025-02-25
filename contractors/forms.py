from django import forms
from .models import Contractor

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'trade', 'phone_number', 'email', 'company']