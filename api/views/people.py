# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import People
from ..serializers.people_serializer import PeopleSerializer

# Create your views here.


@api_view(["GET"])
def index(request):
    people = People.objects.all()
    serializer = PeopleSerializer(people, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def show(request, pk):
    def set_people(people_id):
        try:
            return People.objects.get(id=people_id)
        except People.DoesNotExist:
            return None

    people = set_people(pk)
    if not people:
        return Response(
            {"res": "People does not exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = PeopleSerializer(people)
    return Response(serializer.data, status=status.HTTP_200_OK)
