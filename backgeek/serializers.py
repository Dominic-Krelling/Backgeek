from rest_framework.serializers import ModelSerializer

from backgeek.models import Calca, Camiseta, Chapeu, Tenis

class CalcaSerializer(ModelSerializer):
    class Meta:
        model = Calca
        fields = "__all__"

class CamisetaSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = "__all__"

class ChapeuSerializer(ModelSerializer):
    class Meta:
        model = Chapeu
        fields = "__all__"

class TenisSerializer(ModelSerializer):
    class Meta:
        model = Tenis
        fields = "__all__"