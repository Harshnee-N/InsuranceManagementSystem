from django import forms
from django.contrib.auth.models import User
from .models import Customer, Policy, Claim


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address', 'age']


class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = [
            'name',
            'policy_type',
            'premium_amount',
            'coverage_amount',
            'duration_years',
            'description',
        ]


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['claim_amount', 'reason']