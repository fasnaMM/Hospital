from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from.forms import doctorForm,appointmentForm,patientForm,departmentForm
from.models import Patient,Doctor,Appointment,Department

# Create your views here.

def home(request):
    return render(request,'home.html')
def base(request):
    return render(request,'base.html')
def about(request):
    return render(request,'about.html')
def appointment(request):
    return render(request,'appointment.html')
def service(request):
    return render(request, 'service.html')
def usermodule1(request):
    return render(request,'usermodule1.html')
def admodule(request):
    return render(request,'admodule.html')



def patientregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                #messages.info(request,"username taken")
                return redirect('patientregistration')
                user = User.objects.create_user(username=username,password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return redirect('patientregistration')
        return render(request,'home.html')
    else:
        return render(request,'patientregistration.html')


def doctorregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                # messages.info(request,"username taken")
                return redirect('doctorregistration')
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user created")
        else:
            print("password not matched")
            return redirect('doctorregistration')
        return render(request, 'home.html')
    else:
        return render(request, 'doctorregistration.html')




def doctorlist(request):
    return render(request,'doctorlist.html')
def doctormodule(request):
    return render(request,'Doctormodule.html')
#def adminmodule(request):
    #return render(request,'adminmodule.html')


def department(request):
    if request.method == "POST":
        form = departmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = departmentForm()
    return render(request, 'department.html')

def appointmentnew(request):
    if request.method == "POST":
        form = appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = appointmentForm()
    return render(request, 'appointmentnew.html')
def contact(request):
    return render(request,'contact.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'usermodule.html')
            return render(request, 'login.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'home.html')
           #return render(request,'Adminmodule.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'doctormodule.html')
            return render(request,'login.html')
        except:
             pass
    else:
        return render(request,'login.html')

def deptregistration(request):
        if request.method == "POST":
            form = departmentForm(request.POST)
            if form.is_valid():
                form.save()
            return render(request, 'home.html')
        else:
            form = departmentForm()
        return render(request, 'deptregistration.html')
def adminapprove(request):
    return HttpResponse("<h2>Your Appoinment is Approved</h2>")
def viewpatient(request):
    return render(request,'viewpatient.html')









