"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('login', views.login, name='login'),

    path('patientregistration', views.patientregistration, name='patientregistration'),
    path('doctorregistration', views.doctorregistration, name='doctorregistration'),
    path('appointment', views.appointment, name='appointment'),
    path('service', views.service, name='service'),
    path('appointmentnew', views.appointmentnew, name='appointmentnew'),
    path('usermodule1',views.usermodule1, name='usermodule1'),
    path('doctorlist', views.doctorlist, name='doctorlist'),
    path('department', views.department, name='department'),
    path('doctormodule', views.doctormodule, name='doctormodule'),
    path('contact', views.contact, name='contact'),
    path('admodule', views.admodule, name='admodule'),
    #path('signup', views.contact, name='signup'),
    path('deptregistration', views.deptregistration, name='deptregistration'),
    path('adminapprove', views.adminapprove, name='adminapprove'),
    path('viewpatient',views.viewpatient,name='viewpatient'),

]
