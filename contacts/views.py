from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404
from .models import Company, Employee

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

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