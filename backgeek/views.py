from rest_framework.viewsets import ModelViewSet

from .models import Camiseta, Estampa,Moletom, Produto, Categoria
from .serializers import CamisetaSerializer, CamisetaDetailSerializer, CamisetaListSerializer, EstampaSerializer, MoletomDetailSerializer, MoletomListSerializer, MoletomSerializer, CategoriaSerializer, ProdutoDetailSerializer, ProdutoListSerializer, ProdutoSerializer

class CamisetaViewSet(ModelViewSet):
    queryset = Camiseta.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CamisetaListSerializer
        elif self.action == "retrieve":
            return CamisetaDetailSerializer
        return CamisetaSerializer

class MoletomViewSet(ModelViewSet):
    queryset = Moletom.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MoletomListSerializer
        elif self.action == "retrieve":
            return MoletomDetailSerializer
        return MoletomSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class EstampaViewSet(ModelViewSet):
    queryset = Estampa.objects.all()
    serializer_class = EstampaSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProdutoListSerializer
        elif self.action == "retrieve":
            return ProdutoDetailSerializer
        return ProdutoSerializer
