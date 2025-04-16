from django import forms

class StudentForm(forms.Form):
    SUBJECTS = [
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('English', 'English'),
        ('History', 'History')
    ]
    
    name = forms.CharField(max_length=100, label="Name")
    roll = forms.CharField(max_length=10, label="Roll Number")
    subject = forms.ChoiceField(choices=SUBJECTS, label="Subject")
    mobile_number=forms.CharField(max_length=10, label="Mobile_number")
