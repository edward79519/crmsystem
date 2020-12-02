from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.companys, name='Company'),
    path('company/add/', views.comp_add, name='Add Company'),
    path('company/<int:company_id>/', views.comp_detail, name='Conpany Detail'),
    path('employee/', views.employees, name='Employee'),
    path('employee/add/', views.emp_add, name='Add Employee'),
    path('employee/<int:employee_id>/', views.emp_detail, name='Employee Detail'),
]

