from django.urls import path

from . import views

urlpatterns = [
    path('company/', views.companys, name='index'),
    path('employee/', views.employees, name='index'),
]