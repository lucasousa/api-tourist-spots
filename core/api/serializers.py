from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot
from attraction.api.serializers import AttractionSerializer
from address.api.serializers import AddressSerializer
from comments.api.serializers import CommentSerializer
from evaluations.api.serializers import EvaluationSerializer
from rest_framework.fields import SerializerMethodField
from attraction.models import Attraction
from address.models import Address


class TouristSpotSerializer(ModelSerializer):
    attractions = AttractionSerializer(many=True)
    address = AddressSerializer()
    comments = CommentSerializer(many=True, read_only=True)
    evaluation  = EvaluationSerializer(many=True,read_only=True)
    full_description = SerializerMethodField(read_only=True)

    class Meta:
        model = TouristSpot
        fields = (
                  'id','name', 'description','image', 'attractions', 'comments',
                  'evaluation','address','full_description', 'full_description2'
                )

    def create_attractions(self, attractions, point):
        for attraction in attractions:
            at = Attraction.objects.create(**attraction)
            point.attractions.add(at)

    def create(self, validated_data):
        attractions = validated_data['attractions']
        del validated_data['attractions']
        
        data_address = validated_data['address']
        del validated_data['address']

        point = TouristSpot.objects.create(**validated_data)
        self.create_attractions(attractions, point)
        
        address = Address.objects.create(**data_address)
        point.address = address

        point.save()
        
        return point


    def get_full_description(seçf, obj):
        return '%s - %s' % (obj.name, obj.description)