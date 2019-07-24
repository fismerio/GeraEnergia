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
