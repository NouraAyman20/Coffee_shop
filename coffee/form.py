from django import forms
from .models import Add

class AddCard(forms.ModelForm):
  class Meta:
    model = Add
    fields ='__all__'
    
    
    

