from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    comp_name = models.CharField(max_length=50)
    comp_taxid = models.CharField(max_length=10, primary_key=True)
    comp_catgo = models.CharField(max_length=20)
    comp_leader = models.ForeignKey(
        'Employee',
        on_delete=models.SET_NULL,
        related_name="company",
        null=True,
        blank=True
    )
    comp_address = models.CharField(max_length=100)
    create_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.comp_name


class Employee(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_comp = models.ForeignKey(
        Company,
        on_delete=models.SET_NULL,
        related_name="employee",
        null=True,
        blank=True,
    )
    emp_title = models.CharField(max_length=50)
    emp_tel = models.CharField(max_length=20)
    emp_email = models.EmailField(max_length=254)
    create_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.emp_name


class Opportunity(models.Model):
    opp_name = models.CharField(max_length=100)
    opp_comp = models.ForeignKey(
        Company,
        on_delete=models.DO_NOTHING
    )
    opp_spnsr = models.ForeignKey(
        Employee,
        on_delete=models.DO_NOTHING,
    )

    class ChanceChoice(models.TextChoices):
        HIGH = 'Hi', _("High")
        MEDIUM = 'MD', _("Medium")
        Low = 'LO', _("Low")
    
    chance = models.CharField(
        max_length=2,
        choices=ChanceChoice.choices
    )

    class ProcessChoice(models.TextChoices):
        OPEN = "OP", _("Open")
        ONGOING = "GO", _("On-going")
        CLOSE = "CL", _("Close")
        CANCEL = "CN", _("Cancel")

    process_stage = models.CharField(
        max_length=2,
        choices=ProcessChoice.choices,
        default=ProcessChoice.OPEN
    )

    money = models.DecimalField(max_digits=16, decimal_places=0)
    create_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # create_by = models.CharField(max_length=20)
    start_time = models.DateField(default=timezone.now())
    end_time = models.DateField()


    def __str__(self):
        return self.opp_name