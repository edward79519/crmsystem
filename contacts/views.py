from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Company, Employee
from .form import CompanyModelForm, EmployeeModelForm
from .govcompinfo import Compinfor

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

def emp_add(request):
    form = EmployeeModelForm()
    template = loader.get_template('contacts/emp_form.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

def comp_detail(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    employee = Employee.objects.filter(emp_comp = company_id)
    com_infor = Compinfor(50791838).getinfo()[0]
    context = {
        'company': company,
        'employee': employee,
        'com_infor': com_infor,
    }
    return render(request, 'contacts/comp_detail.html', context)

def emp_detail(request, employee_id):
    return HttpResponse("You're looking at employee %s." % employee_id)