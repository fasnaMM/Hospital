# Generated by Django 5.0.2 on 2024-03-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentnumber', models.CharField(max_length=200)),
                ('departmentname', models.CharField(max_length=200, null=True)),
                ('doctorname', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
