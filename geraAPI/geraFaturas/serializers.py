from rest_framework import  serializers 
from geraFaturas.models import Distribuidora, Cliente, Fatura 


# Serializers define the API representation.
class DistribuidoraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Distribuidora
		fields = '__all__'
		# fields = ('nome')

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = '__all__'

class FaturaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Fatura
		fields = '__all__'


# Add Distribuidora e Fatura aggregates
class ClienteInfoSerializer(serializers.ModelSerializer):
	fatura_min = serializers.IntegerField()
	fatura_avg = serializers.IntegerField()
	fatura_max = serializers.IntegerField()
	distribuidora_nome = serializers.CharField()

	class Meta:
		model = Cliente
		# fields = ('fatura_min','nome', 'numero', 'distribuidora')
		fields = '__all__'

