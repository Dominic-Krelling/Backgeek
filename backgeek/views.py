from rest_framework.viewsets import ModelViewSet

from .models import Camiseta, Estampa,Moletom
from .serializers import CamisetaSerializer, CamisetaDetailSerializer, CamisetaListSerializer, EstampaSerializer, MoletomDetailSerializer, MoletomListSerializer, MoletomSerializer

class CamisetaViewSet(ModelViewSet):
    queryset = Camiseta.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CamisetaListSerializer
        elif self.action == "retrieve":
            return CamisetaDetailSerializer
        return CamisetaSerializer
    
class EstampaViewSet(ModelViewSet):
    queryset = Estampa.objects.all()
    serializer_class = EstampaSerializer

class MoletomViewSet(ModelViewSet):
    queryset = Moletom.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MoletomListSerializer
        elif self.action == "retrieve":
            return MoletomDetailSerializer
        return MoletomSerializer
    