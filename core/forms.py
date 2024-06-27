from django import forms
from .models import Account


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
            
class CreateAccountForm(forms.Form):
    class Meta:
        model = Account
        fields = ["account_name", "balance"]