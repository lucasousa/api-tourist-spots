from rest_framework.serializers import ModelSerializer
from address.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = ['line1', 'line2', 'city', 'state', 'country', 
                  'latitude', 'longitude']