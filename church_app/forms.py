from django import forms
from .models import Member, FirstTimer

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{10}', 'placeholder': '10-digit phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_joined': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class FirstTimerForm(forms.ModelForm):
    class Meta:
        model = FirstTimer
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{10}', 'placeholder': '10-digit phone number'}),
            'invited_by': forms.TextInput(attrs={'class': 'form-control'}),
            'service_feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'born_again': forms.Select(attrs={'class': 'form-select'}),
            'would_like_visit': forms.Select(attrs={'class': 'form-select'}),
            'available_for_fellowship': forms.Select(attrs={'class': 'form-select'}),
            'date_visited': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
