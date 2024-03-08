from.models import Patient,Doctor,Appointment,Department,Login
from django import forms

class patientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        widgets={
            
        }

class doctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {

        }

class appointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields="__all__"
        widgets={

        }
class departmentForm(forms.ModelForm):
    class Meta:
        model =Department
        fields="__all__"
        widgets={

        }
class loginForm(forms.ModelForm):
    class Meta:
         model = Login
         fields = "__all__"
         widgets={

         }
