# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from ..models import Family
from ..serializers import FamilySerializer


@api_view(["GET"])
def index(request):
    families = Family.objects.prefetch_related("persons").all()
    serializer = FamilySerializer(families, many=True)
    return Response({"families": serializer.data}, status=status.HTTP_200_OK)


@api_view(["GET"])
def show(request, pk):
    def set_family(family_id):
        try:
            return Family.objects.prefetch_related("persons").get(id=family_id)
        except Family.DoesNotExist:
            return None

    family = set_family(pk)
    if not family:
        return Response(
            {"res": "Family does not exists"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = FamilySerializer(family)
    return Response({"family": serializer.data}, status=status.HTTP_200_OK)
