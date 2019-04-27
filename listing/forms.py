from django import forms
from .models import Search
from bootstrap_datepicker_plus import DatePickerInput

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('destination', 'from_date','to_date','num_guests')
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'from_date': forms.DateInput(attrs={'class': 'form-control date'}, format='%d-%m-%y'),
            'to_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Check-Out Date'}),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'})
        }
