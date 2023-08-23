from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from backgeek.models import Camiseta


class CamisetaSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = "__all__"
    imagem_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

class CamisetaDetailSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = "__all__"
        depth = 1
        imagem = ImageSerializer(required = False)

class CamisetaListSerializer(ModelSerializer):
    class Meta:
        model = Camiseta
        fields = ["id", "modelo", "preco"]