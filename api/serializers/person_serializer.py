from rest_framework.serializers import ModelSerializer
from ..models import Person
from .family_person_serializer import FamilyPersonSerializer


class PersonSerializer(ModelSerializer):
    family_relations = FamilyPersonSerializer(source="get_relation_type", many=True)

    class Meta:
        model = Person
        fields = "__all__"
