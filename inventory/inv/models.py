from django.db import models
from django.utils import timezone

class Items(models.Model):
    name = models.CharField(default="*name*", max_length=100)
    desc = models.TextField(default="*item*")
    type = models.CharField(default="*type*", max_length=100)
    num = models.PositiveSmallIntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)