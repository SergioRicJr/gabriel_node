from rest_framework import serializers
from .models import GabrielNode

class GabrielNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GabrielNode
        fields = ['id', 'sensor', 'botao', 'liga_robo', 'reset_contador', 'valor_contagem']
