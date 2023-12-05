from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer, SlugRelatedField, CharField

from uploader.models import Image
from uploader.serializers import ImageSerializer

from backgeek.models import Camiseta, Estampa, Moletom, Produto, Categoria


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
        fields = ["id", "descricao", "titulo", "preco", "first_image"]

class EstampaSerializer(ModelSerializer):
    class Meta:
        model = Estampa
        fields = "__all__"

class MoletomSerializer(ModelSerializer):
    class Meta:
        model = Moletom
        fields = "__all__"
    imagem_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)

class MoletomDetailSerializer(ModelSerializer):
    class Meta:
        model = Moletom
        fields = "__all__"
        depth = 1
        imagem = ImageSerializer(required = False)

class MoletomListSerializer(ModelSerializer):
    class Meta:
        model = Moletom
        fields = ["id", "descricao", "titulo", "preco", "first_image"]


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProdutoSerializer(ModelSerializer):
    capa_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    capa = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1


class ProdutoListSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ["id", "titulo", "preco"]


class ProdutoDetailSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = "__all__"
        depth = 1
        capa = ImageSerializer(required=False)