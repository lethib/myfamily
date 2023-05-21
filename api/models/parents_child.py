# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .people import People


class ParentsChild(models.Model):
    first_parent_id = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name="first_parent"
    )
    second_parent_id = models.ForeignKey(
        People, on_delete=models.CASCADE, related_name="second_parent"
    )
    child_id = models.ForeignKey(People, on_delete=models.CASCADE, related_name="child")
