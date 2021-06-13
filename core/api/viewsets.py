from rest_framework import viewsets
from core.api.serializers import TouristSpotSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from core.models import TouristSpot
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication


class TouristSpotViewSet(viewsets.ModelViewSet):
    permission_classes=(DjangoModelPermissions,) #dá as mesmas permissões dada ao usuário no django admin
    authentication_classes=(TokenAuthentication,)
    serializer_class = TouristSpotSerializer
    filter_backends = (SearchFilter, )
    search_fields = ('name','description')
    #lookup_field='name' #agora irá buscar pelo name ao invés do id (o padrão é o id), porém, para substituir o padrão, deve-se passar um campo que seja único

    def get_queryset(self):
        queryset = TouristSpot.objects.all()
        id_point = self.request.query_params.get('id', None) #Esse none é pra caso não venha um id na url não parar a aplicação
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if id_point:
            queryset = TouristSpot.objects.filter(id=id_point)

        if name:
            queryset = queryset.filter(name__iexact=name)

        if description:
            queryset = queryset.filter(description__iexact=description)#Esse lookup iexact serve pra desconsiderar case sensitive
        
        return queryset
    
    #O comportamento padrão é o get_queryset, mas eu posso criar o meu comportamento desejado
    #sobrescrevendo o método list
    def list(self, request, *args,**kwargs):
        return super(TouristSpotViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(TouristSpotViewSet, self).create(request, *args, **kwargs)
    
    def retrieve(self, request, *args,**kwargs):
        return super(TouristSpotViewSet, self).retrieve(request, *args, **kwargs)

    def destroy(self, request, *args,**kwargs):
        return super(TouristSpotViewSet, self).destroy(request, *args, **kwargs)

    def update(self, request, *args,**kwargs):
        return super(TouristSpotViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args,**kwargs):
        return super(TouristSpotViewSet, self).partial_update(request, *args, **kwargs)
  

    #actions personalizadas
    #tem que passar detail igual a True pra ele poder passar o parâmetro pk
    @action(methods=['get'], detail=True)
    def denounce(self, request, pk=None):
        pass

    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass



#Métodos do compormento padrão:
# - list
# - create
# - destroy
# - retrive
# - update
# - partial_update