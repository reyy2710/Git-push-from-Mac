from django import forms
from .models import Employee

class EmployeeForm(forms.Form):
    emp_id = forms.ModelChoiceField(queryset=Employee.objects.all(), empty_label="Select Employee")
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
