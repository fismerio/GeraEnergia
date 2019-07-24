from django.db import models

class Distribuidora(models.Model):

	class Meta:
		db_table = 'distribuidora'

	nome = models.CharField(max_length=200)

	def __str__(self):
		return self.nome 

class Cliente(models.Model):

	class Meta:
		db_table = 'cliente'

	nome = models.CharField(max_length=200) 
	numero = models.IntegerField() 
	distribuidora = models.ForeignKey('Distribuidora', related_name=’clientes’, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nome

class Fatura(models.Model):

	class Meta:
		db_table = 'fatura' 

	referencia = models.DateField()          				#date
	valor = models.models.FloatField()						#float
	cliente = models.ForeignKey('Cliente', related_name=’faturas’, on_delete=models.CASCADE)

	#need str method?
	#need class Meta?