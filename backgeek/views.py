from rest_framework.viewsets import ModelViewSet

from .models import Calca, Camiseta, Chapeu, Tenis
from .serializers import CalcaSerializer, CamisetaSerializer, ChapeuSerializer, TenisSerializer

class CalcaViewSet(ModelViewSet):
    queryset = Calca.objects.all()
    serializer_class = CalcaSerializer

class CamisetaViewSet(ModelViewSet):
    queryset = Camiseta.objects.all()
    serializer_class = CamisetaSerializer

class ChapeuViewSet(ModelViewSet):
    queryset = Chapeu.objects.all()
    serializer_class = ChapeuSerializer

class TenisViewSet(ModelViewSet):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer