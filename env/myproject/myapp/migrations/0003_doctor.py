# Generated by Django 5.0.2 on 2024-03-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_patient_email_patient_age_patient_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=200)),
                ('speciality', models.CharField(max_length=250)),
                ('age', models.CharField(max_length=200, null=True)),
                ('Email', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200, null=True)),
                ('contact', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('days', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=200)),
            ],
        ),
    ]
