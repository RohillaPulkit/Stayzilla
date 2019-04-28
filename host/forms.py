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
        fields = ('name', 'description' , 'house_rules' , 'accommodates' ,
                  'cancellation_policy', 'room_type','property_type','amenities',
                  'picture_url','city', 'state', 'street', 'zip_code', 'start_date', 'end_date', 'price')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your listing'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Brief description of your listing'}),
            'house_rules': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'House Rules'}),
            'accommodates': forms.NumberInput(attrs={'class': 'form-control',
                                                     'placeholder': 'Enter number of maximum guests'}),
            'cancellation_policy': forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Cancellation Policy of the listing'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Type of room available'
                                                }),
            'property_type': forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder': 'Type of property available'
                                                    }),
            'amenities': forms.Textarea(attrs={'class': 'form-control',
                                                'placeholder': 'Amenities offered'
                                                }),
            'picture_url': forms.URLInput(attrs={'class': 'form-control',
                                                 'placeholder': 'Attract guests with a picture'
                                                 }),
            'city': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'City'
                                                }),
            'state': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'State'
                                                }),
            'street': forms.TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Street Address'
                                                }),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Zip/Postal Code'
                                                }),
            'start_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Available from date'},
                                          options={
                                                "format": "DD-MMM-YY",  # moment date-time format
                                                "showClose": False,
                                                "showClear": False,
                                                "showTodayButton": False,
                                          }
                                          ),
            'end_date': DatePickerInput(attrs={'class': 'form-control', 'placeholder': 'Available till date'},
                                        options={
                                           "format": "DD-MMM-YY",  # moment date-time format
                                           "showClose": False,
                                           "showClear": False,
                                           "showTodayButton": False,
                                       }
                                       ),
            'price': forms.NumberInput(attrs={'class': 'form-control',
                                                'placeholder': 'Price per listing'
                                                }),
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

