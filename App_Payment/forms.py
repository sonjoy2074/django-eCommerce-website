from django import forms
from App_Payment.models import BillingAddress



class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['address', 'zipcode', 'city', 'country']
        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'zipcode': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
        }