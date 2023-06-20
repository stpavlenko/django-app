from django import forms
from .models import Reservation, Table


class ReservationForm(forms.ModelForm):
    table = forms.ModelChoiceField(
        queryset=Table.objects.all(), empty_label=None)

    class Meta:
        model = Reservation
        fields = ['table', 'date', 'start_time', 'end_time']
        # Дополнительные поля, если необходимо
