from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    MANUFACTURERS = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes')
    ]

    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label="Car Manufacturer")

    class Meta:
        model = Car
        fields = ['manufacturer', 'model_name']
