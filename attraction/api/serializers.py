from rest_framework.serializers import ModelSerializer
from attraction.models import Attraction


class AttractionSerializer(ModelSerializer):
    class Meta:
        model = Attraction
        fields = ('name', 'description', 'businnes_hours', 'minimum_age', 'image')