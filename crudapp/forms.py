from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "symptoms"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter your name'}),
            'age': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Enter your age'}),
            'symptoms': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. fever, cold'}),
        }