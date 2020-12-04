from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.companys, name='Company'),
    path('company/add/', views.comp_add, name='Add Company'),
    path('company/<int:company_id>/', views.comp_detail, name='CompanyDetail'),
    path('company/<int:company_id>/update/', views.comp_update, name="CompanyUpdate"),
    path('company/<int:company_id>/delete/', views.comp_delete, name="CompanyDelete"),
    path('employee/', views.employees, name='Employee'),
    path('employee/add/', views.emp_add, name='AddEmployee'),
    path('employee/<int:employee_id>/', views.emp_detail, name='EmployeeDetail'),
    path('employee/<int:employee_id>/update', views.emp_update, name='EmployeeUpdate'),
    path('employee/<int:employee_id>/delete', views.emp_delete, name='EmployeeDelete'),
]

