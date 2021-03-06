# Generated by Django 3.1.3 on 2020-11-18 03:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('comp_name', models.CharField(max_length=50)),
                ('comp_taxid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('comp_catgo', models.CharField(max_length=20)),
                ('comp_address', models.CharField(max_length=100)),
                ('create_date', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_title', models.CharField(max_length=50)),
                ('emp_tel', models.CharField(max_length=20)),
                ('emp_email', models.EmailField(max_length=254)),
                ('create_date', models.TimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('emp_comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee', to='contacts.company')),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opp_name', models.CharField(max_length=100)),
                ('chance', models.CharField(choices=[('Hi', 'High'), ('MD', 'Medium'), ('LO', 'Low')], max_length=2)),
                ('process_stage', models.CharField(choices=[('OP', 'Open'), ('GO', 'On-going'), ('CL', 'Close'), ('CN', 'Cancel')], default='OP', max_length=2)),
                ('money', models.DecimalField(decimal_places=0, max_digits=16)),
                ('start_time', models.DateField(default=datetime.datetime(2020, 11, 18, 3, 27, 21, 644596, tzinfo=utc))),
                ('end_time', models.DateField()),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('opp_comp', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.company')),
                ('opp_spnsr', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.employee')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='comp_leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='contacts.employee'),
        ),
        migrations.AddField(
            model_name='company',
            name='create_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
