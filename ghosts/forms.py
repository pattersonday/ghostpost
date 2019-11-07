from django import forms
from .models import BoastsAndRoasts


class BoastsAndRoastsAddForm(forms.ModelForm):
    class Meta:
        model = BoastsAndRoasts
        fields = [
            'is_boast',
            'content',
            'upvote',
            'downvote',
            'post_date'
        ]
        widgets = {
            'Roast': forms.RadioSelect
        }


form = BoastsAndRoastsAddForm()
