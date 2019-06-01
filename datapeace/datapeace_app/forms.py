from .models import UserData
from django.contrib.auth import authenticate
from django import forms
import datapeace.form_validators as form_validators


class UserCreationForm(forms.Form):

    first_name = forms.CharField(max_length=100, error_messages={
        'required': 'First Name is required',
        'max_length': 'First Name should not be more than 100 characters'
    })

    last_name = forms.CharField(max_length=100, error_messages={
        'required': 'Last Name is required',
        'max_length': 'Last Name should not be more than 100 characters'
    })

    company_name = forms.CharField(max_length=200, error_messages={
        'required': 'Company Name is required',
        'max_length': 'Company Name should not be more than 200 characters'
    })

    age = forms.IntegerField(min_value=1,
                             error_messages={
                                 'invalid': 'Please enter a positive numeric value',
                                 'min_value': 'Please enter a positive numeric value',
                             })

    city = forms.CharField(max_length=100, error_messages={
        'required': 'City is required',
        'max_length': 'City should not be more than 100 characters'
    })

    state = forms.CharField(max_length=100, error_messages={
        'required': 'State is required',
        'max_length': 'State should not be more than 100 characters'
    })

    zip = forms.CharField(validators=[form_validators.zipcode_validator], error_messages={
        'required': 'Zip is required'
    })

    email = forms.EmailField(max_length=254,
                             error_messages={
                                 'required': 'Email id is required',
                                 'invalid': 'Invalid email id provided',
                                 'max_length': 'Email id should not be more than 254 characters',
                             })

    web = forms.CharField(max_length=200,validators=[form_validators.website_address_validator], error_messages={
        'required': 'Website is required',
        'max_length': 'Website should not be more than 200 characters'
    })

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name', '').strip()
        if not first_name:
            raise forms.ValidationError('Please Enter a valid First Name')
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name', '').strip()
        if not last_name:
            raise forms.ValidationError('Please Enter a valid Last Name')
        return last_name

    def clean_company_name(self):
        company_name = self.cleaned_data.get('company_name', '').strip()
        if not company_name:
            raise forms.ValidationError('Please Enter a valid Company name')
        return company_name

    def clean_city(self):
        city = self.cleaned_data.get('city', '').strip()
        if not city:
            raise forms.ValidationError('Please Enter a valid city')
        return city

    def clean_state(self):
        state = self.cleaned_data.get('state', '').strip()
        if not state:
            raise forms.ValidationError('Please Enter a valid state')
        return state

    def clean_web(self):
        web = self.cleaned_data.get('web', '').strip()
        if not web:
            raise forms.ValidationError('Please Enter a valid state')
        return web



