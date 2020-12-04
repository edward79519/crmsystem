from django.shortcuts import render, redirect
from django import forms
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Company, Employee
from .form import CompanyModelForm, EmployeeModelForm
from .govcompinfo import Compinfor
from django.contrib.auth.decorators import login_required

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

# Write
@login_required
def comp_add(request):
    form = CompanyModelForm()
    template = loader.get_template('contacts/comp_form.html')
    if request.method == "POST":
        form = CompanyModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/companys")
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

@login_required
def emp_add(request):
    form = EmployeeModelForm()
    template = loader.get_template('contacts/emp_form.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

# Read
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
    employee = get_object_or_404(Employee, pk=employee_id)
    company = Company.objects.get(comp_name=employee.emp_comp)
    context = {
        'employee': employee,
        'company': company,
    }
    return render(request, 'contacts/emp_detail.html', context)

# Update
@login_required
def comp_update(request, company_id):
    company = Company.objects.get(pk=company_id)
    form = CompanyModelForm(instance=company)
    template = loader.get_template('contacts/comp_update.html')
    # form.widgets['comp_taxid'] = forms.HiddenInput()
    if request.method == "POST":
        form = CompanyModelForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
        return redirect("/contacts/company/"+str(company_id))
    context = {
        'form': form
    }

    return HttpResponse(template.render(context, request))

# Delete
@login_required
def comp_delete(request, company_id):
    company = Company.objects.get(pk=company_id)
    template = loader.get_template('contacts/comp_delete.html')

    if request.method == "POST":
        company.delete()
        return redirect("/contacts/company/")

    context = {
        'company': company
    }
    return HttpResponse(template.render(context, request))