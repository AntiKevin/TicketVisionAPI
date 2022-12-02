from rest_framework import serializers
from .models import AdminsExtra, Areas, Chamados

class AdminsExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminsExtra
        fields = ['cargo', 'area', 'vinculo', 'user']
        
class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = ['nome']
        
class ChamadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamados
        fields = ['nome', 'setor', 'titulo', 'descricao', 'prior', 'status', 'data', 'areas']