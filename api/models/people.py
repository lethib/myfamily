# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class People(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female"), ("U", "Undefined")]
    )
    date_birth = models.DateField()
    date_death = models.DateField(null=True, blank=True)
