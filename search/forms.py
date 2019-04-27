from django import forms
from .models import Search
from bootstrap_datepicker_plus import DatePickerInput


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('destination', 'from_date','to_date','num_guests')
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'from_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-In'}),
            'to_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-Out'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'})
        }
