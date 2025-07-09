# forms.py
from django import forms
from .models import Booking, Table
from django.utils import timezone

class TableReservationForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['name', 'email', 'date', 'time', 'phone', 'people', 'message']

    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now():
            raise forms.ValidationError("The reservation date cannot be in the past.")
        return date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'subject', 'message']
