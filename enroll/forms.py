from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['name','email','date_of_birth','gender','parent_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=User.gender_choices, attrs={'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

