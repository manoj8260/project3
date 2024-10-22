from django import forms
from .models import *
class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']
        help_texts={'username':' '}
        

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model= CustomerProfile
        exclude=['username']
