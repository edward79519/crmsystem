from django import forms
from .models import Company

class CompanyModelForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'comp_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Name'}),
            'comp_taxid': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': '00000000'}),
            'comp_catgo': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Category'}),
            'comp_leader': forms.Select(attrs={'class': 'custom-select'}),
            'comp_address': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Address'}),
            'create_by': forms.Select(attrs={'class': 'custom-select'}),
        }