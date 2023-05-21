from rest_framework.serializers import ModelSerializer
from ..models import Family
from .people_serializer import PeopleSerializer


class FamilySerializer(ModelSerializer):
    first_parents_data = PeopleSerializer(source="first_family_parent_id")
    second_parents_data = PeopleSerializer(source="second_family_parent_id")

    class Meta:
        model = Family
        fields = "__all__"
