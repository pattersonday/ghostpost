from django.db import models
from django.utils import timezone

BOOL_CHOICES = ((True, 'Roast'), (False, 'Boast'))


class BoastsAndRoasts(models.Model):

    is_boast = models.BooleanField(choices=BOOL_CHOICES)
    content = models.CharField(max_length=280)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    post_date = models.DateTimeField(default=timezone.now)
