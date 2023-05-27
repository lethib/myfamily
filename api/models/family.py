# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .person import Person


class Family(models.Model):
    """Families are groups of persons with parents and children"""

    name = models.CharField(max_length=30)
    persons = models.ManyToManyField("Person", through="FamilyPerson")

    def get_persons_data(self):
        return Person.objects.filter(families=self)
