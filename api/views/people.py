# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Person
from ..serializers import PersonSerializer

# Create your views here.


@api_view(["GET"])
def index(request):
    people = Person.objects.all()
    serializer = PersonSerializer(people, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def show(request, pk):
    def set_people(people_id):
        try:
            return Person.objects.get(id=people_id)
        except Person.DoesNotExist:
            return None

    people = set_people(pk)
    if not people:
        return Response(
            {"res": "People does not exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = PersonSerializer(people)
    return Response(serializer.data, status=status.HTTP_200_OK)
