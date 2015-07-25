from django import forms
from . import models

class ConnexionForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username','password']

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['username','password','email']

        widgets = {'password':forms.PasswordInput()}
