from rest_framework.serializers import ModelSerializer
from ..models import FamilyPerson


class FamilyPersonSerializer(ModelSerializer):
    class Meta:
        model = FamilyPerson
        fields = "__all__"
