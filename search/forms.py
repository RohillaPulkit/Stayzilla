from django import forms
from .models import Search
from bootstrap_datepicker_plus import DatePickerInput


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('destination', 'from_date', 'to_date', 'num_guests')
        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Destination'}),
            'from_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-In'},
                                         options={
                                             "format": "DD-MMM-YY",  # moment date-time format
                                             "showClose": False,
                                             "showClear": False,
                                             "showTodayButton": False,
                                         }
                                         ),
            'to_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Check-Out'},
                                       options={
                                           "format": "DD-MMM-YY",  # moment date-time format
                                           "showClose": False,
                                           "showClear": False,
                                           "showTodayButton": False,
                                       }
                                       ),
            'num_guests': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of Guests'})
        }
