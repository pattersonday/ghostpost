from django import forms
from .models import BoastsAndRoasts


class BoastsAndRoastsAddForm(forms.ModelForm):
    class Meta:
        model = BoastsAndRoasts
        fields = [
            'is_boast',
            'content'
        ]
        widgets = {
            'is_boast': forms.RadioSelect
        }


form = BoastsAndRoastsAddForm()
