# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Person, Family, FamilyPerson

admin.site.register([Person, Family, FamilyPerson])
