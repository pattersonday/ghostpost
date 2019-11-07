from django.db import models
from django.utils import timezone
from djchoices import ChoiceItem, DjangoChoices


class BoastsAndRoasts(models.Model):

    class BoastOrRoast(DjangoChoices):
        boasts_or_roasts = ChoiceItem('boasts', 'roasts')

    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=280, choices=BoastOrRoast.choices)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
