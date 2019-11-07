from django import forms
from .models import BoastsAndRoasts


class BoastsAndRoastsAddForm(forms.ModelForm):
    class Meta:
        model = BoastsAndRoasts
        fields = [
            'boasts_or_roasts',
            'is_boasts',
            'content',
            'upvote',
            'downvote',
            'post_date'
        ]


form = BoastsAndRoastsAddForm()
