from rest_framework.viewsets import ModelViewSet

from .models import Camiseta
from .serializers import CamisetaSerializer, CamisetaDetailSerializer, CamisetaListSerializer

class CamisetaViewSet(ModelViewSet):
    queryset = Camiseta.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CamisetaListSerializer
        elif self.action == "retrieve":
            return CamisetaDetailSerializer
        return CamisetaSerializer