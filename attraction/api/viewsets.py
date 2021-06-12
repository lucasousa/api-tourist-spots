from rest_framework import viewsets
from attraction.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer
    filter_fields = ('name', 'description') #django filter - filtro por nome e descrição de uma atração