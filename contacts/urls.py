from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/', views.companys, name='Company'),
    path('company/add/', views.comp_add, name='Add Company'),
    path('employee/', views.employees, name='Employee'),
]