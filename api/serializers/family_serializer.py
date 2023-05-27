from rest_framework.serializers import ModelSerializer
from ..models import Family
from .person_serializer import PersonSerializer


class FamilySerializer(ModelSerializer):
    persons = PersonSerializer(source="get_persons_data", many=True)

    class Meta:
        model = Family
        fields = "__all__"
