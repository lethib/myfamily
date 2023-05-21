# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .people import People


class Family(models.Model):
    first_family_parent_id = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name="first_family_parent"
    )
    second_family_parent_id = models.ForeignKey(
        People,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="second_family_parent",
    )
    name = models.CharField(max_length=15)
