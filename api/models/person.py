# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .family_person import FamilyPerson

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(
        max_length=1, choices=[("M", "Male"), ("F", "Female"), ("U", "Undefined")]
    )
    date_birth = models.DateField()
    date_death = models.DateField(null=True, blank=True)
    families = models.ManyToManyField("Family", through="FamilyPerson")

    def get_relation_type(self):
        return FamilyPerson.objects.filter(person=self)
