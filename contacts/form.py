from django import forms
from .models import Company, Employee

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


class EmployeeModelForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Name'}),
            'emp_comp': forms.Select(attrs={'class': 'custom-select'}),
            'emp_title': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': 'Title'}),
            'emp_tel': forms.TextInput(attrs={'class': 'form-control is-valid', 'placeholder': '+886-XXX-XXXXXX'}),
            'emp_email': forms.EmailInput(attrs={'class': 'form-control is-valid', 'placeholder': 'example@com.tw'}),
            'create_by': forms.Select(attrs={'class': 'custom-select'})
        }