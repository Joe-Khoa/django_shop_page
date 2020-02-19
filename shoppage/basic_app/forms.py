
from django import forms
from basic_app.models import Customers

class Customers_form(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'
