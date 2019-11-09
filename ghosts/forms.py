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
            'boast_or_roast': forms.RadioSelect
        }


form = BoastsAndRoastsAddForm()
