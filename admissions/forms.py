from django import forms
from django.db import models
from django.forms import widgets
from .models import Admission

class Admission_form(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('name','course','email','mobile',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'course': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
        }