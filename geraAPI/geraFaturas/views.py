# from django.shortcuts import render
from rest_framework import generics
from geraFaturas.models import Distribuidora, Cliente, Fatura  
from .serializers import DistribuidoraSerializer, ClienteSerializer, FaturaSerializer

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
