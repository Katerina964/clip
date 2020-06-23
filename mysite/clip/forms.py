from django import forms

from .models import Ordershop

class OrdershopForm(forms.ModelForm):

    class Meta:
        model = Ordershop
        fields = ('first_name', 'surname', 'town', 'phone', 'email', 'date_order')


