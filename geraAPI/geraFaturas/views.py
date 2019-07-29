# from django.shortcuts import render
from rest_framework import generics
from geraFaturas.models import Distribuidora, Cliente, Fatura
from django.db.models import Avg, Min, Max, F
from .serializers import DistribuidoraSerializer, ClienteSerializer, FaturaSerializer, ClienteInfoSerializer


# Create your views here.
class DistribuidoraList(generics.ListCreateAPIView):
	queryset = Distribuidora.objects.all()
	serializer_class = DistribuidoraSerializer

class DistribuidoraDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Distribuidora.objects.all()
	serializer_class = DistribuidoraSerializer

class ClienteList(generics.ListCreateAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

class FaturaList(generics.ListCreateAPIView):
	queryset = Fatura.objects.all()
	serializer_class = FaturaSerializer

class FaturaDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Fatura.objects.all()
	serializer_class = FaturaSerializer

# Add info to ClientList 
class ClienteListInfo(generics.ListCreateAPIView):
	# queryset = Cliente.objects.all()
	# queryset = Cliente.objects.annotate(min('fatura__valor'))
	queryset = Cliente.objects.all().select_related(
            'distribuidora',
        ).prefetch_related(
            'faturas',
        ).annotate(fatura_min = Min('faturas__valor'),
        fatura_avg = Avg('faturas__valor'),
        fatura_max = Max('faturas__valor'),
        distribuidora_nome = F('distribuidora__nome')
        )

	# queryset = Cliente.objects.all().select_related('distribuidora',).prefetch_related('faturas')
	
	serializer_class = ClienteInfoSerializer

