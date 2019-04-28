from django import forms
from .models import NewListing
from bootstrap_datepicker_plus import DatePickerInput


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
# GUEST_CHOICES = (
#     ('1','1'),
#     ('2', '2'),
#     ('3', '3'),
#     ('4', '4'),
# )


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



