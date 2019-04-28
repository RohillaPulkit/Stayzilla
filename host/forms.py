from django import forms
from .models import NewListing
from bootstrap_datepicker_plus import DatePickerInput
from datetime import datetime, date, timedelta
from django.shortcuts import render, HttpResponse

ROOM_CHOICES = (
    ('private_room','PRIVATE ROOM'),
    ('shared_room', 'SHARED ROOM'),
    ('entire_place', 'ENTIRE PLACE'),
)

PROPERTY_CHOICES = (
    ('apartment','APARTMENT'),
    ('condominium', 'CONDOMINIUM'),
    ('guest_suite', 'GUEST SUITE'),
    ('house', 'HOUSE'),
)


class HostForm(forms.ModelForm):
    class Meta:
        model = NewListing
        fields = ('name', 'description' , 'house_rules' , 'accommodates' , 'cancellation_policy','room_type','property_type','amenities','picture_url','city','state','street','zip_code','start_date','end_date','price' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'house_rules': forms.TextInput(attrs={'class': 'form-control'}),
            'accommodates': forms.NumberInput(attrs={'class': 'form-control'}),
            'cancellation_policy': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control'}),
            'property_type': forms.TextInput(attrs={'class': 'form-control'}),
            'amenities': forms.TextInput(attrs={'class': 'form-control'}),
            'picture_url': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'start_date': DatePickerInput(attrs={'class': 'form-control'}),
            'end_date': DatePickerInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

def clean(self):
    print('called')
    form_data = self.cleaned_data

    today = datetime.now()
    today = today.replace(hour=0, minute=0, second=0, microsecond=0).date()

    from_date_string = form_data.get('start_date')
    to_date_string = form_data.get('end_date')

    from_date = datetime.strptime(from_date_string, '%d-%m-%y').date()
    to_date = datetime.strptime(to_date_string, '%d-%m-%y').date()

    if from_date < today or to_date < today:
        self._errors["Invalid Date"] = "Dates cannot be in past."
        return HttpResponse("please enter valid dates")
        return form_data

    if from_date >= to_date:
        self._errors["Invalid Date"] = "Check-In cannot be greater than or equal to Check-Out."
        return HttpResponse("please enter valid dates")
        return form_data

    return form_data

