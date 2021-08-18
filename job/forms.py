from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Company


class CompanyRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Company
        fields = UserCreationForm.Meta.fields + ('phone','email','address')

    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['username', 'phone', 'email', 'description', 'image']
