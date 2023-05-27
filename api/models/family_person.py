# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FamilyPerson(models.Model):
    """Many-to-Many relationship of Families and Person"""

    person = models.ForeignKey(
        "Person", related_name="persons", on_delete=models.CASCADE
    )
    family = models.ForeignKey(
        "Family", related_name="families", on_delete=models.CASCADE
    )
    relation_type = models.CharField(
        max_length=1, choices=[("P", "Parent"), ("C", "Children")]
    )
