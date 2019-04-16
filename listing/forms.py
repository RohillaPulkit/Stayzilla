from django import forms
from .models import Search


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('destination', 'from_date','to_date','num_guests')
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'from_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check-In Date'}),
            'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check-Out Date'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'})
        }
