from django.contrib import admin

# Register your models here.
from .models import Company, Employee, Opportunity


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('comp_name', 'comp_taxid', 'comp_leader', 'create_date')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'emp_comp', 'emp_email', 'create_date')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Opportunity)