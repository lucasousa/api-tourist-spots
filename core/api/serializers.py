from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot
from attraction.api.serializers import AttractionSerializer
from address.api.serializers import AddressSerializer
from comments.api.serializers import CommentSerializer
from evaluations.api.serializers import EvaluationSerializer
from rest_framework.fields import SerializerMethodField

class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()
    comments = CommentSerializer(many=True)
    evaluation  = EvaluationSerializer(many=True)
    full_description = SerializerMethodField()

    class Meta:
        model = TouristSpot
        fields = (
                  'id','name', 'description','image', 'attractions', 'comments',
                  'evaluation','address','full_description', 'full_description2'
                )

    def get_full_description(seçf, obj):
        return '%s - %s' % (obj.name, obj.description)