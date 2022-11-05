# Generated by Django 3.2.13 on 2022-10-23 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentsMonth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('buyer_category', models.CharField(max_length=255)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('value', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(null=True, upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=30)),
                ('sales', models.CharField(max_length=30)),
                ('departments', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departments', to='profit_and_loss.departments')),
            ],
        ),
    ]
