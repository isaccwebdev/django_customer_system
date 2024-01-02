from django.forms import ModelForm
from .models import CustomerModel

class CustomerForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = ['name','email','url', 'subscribed']
        
    