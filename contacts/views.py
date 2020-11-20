from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Company, Employee
from .form import CompanyModelForm

def index(request):
    template = loader.get_template('contacts/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def companys(request):
    comp_list = Company.objects.order_by('-create_date')
    template = loader.get_template('contacts/company.html')
    context = {
        'comp_list' : comp_list,
    }
    return HttpResponse(template.render(context, request))

def employees(request):
    emp_list = Employee.objects.order_by('-create_date')
    template = loader.get_template('contacts/employee.html')
    context = {
        'emp_list' : emp_list,
    }
    return HttpResponse(template.render(context, request))

def comp_add(request):
    form = CompanyModelForm()
    template = loader.get_template('contacts/comp_form.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))
