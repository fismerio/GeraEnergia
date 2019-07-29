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
	# numero = models.IntegerField() 
	numero =  models.CharField(max_length=200)  
	distribuidora = models.ForeignKey('Distribuidora', related_name='clientes', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nome

class Fatura(models.Model):

	class Meta:
		db_table = 'fatura' 

	# referencia = models.DateField()          				#date
	cliente = models.ForeignKey('Cliente', related_name='faturas', on_delete=models.CASCADE)	
	valor = models.FloatField()						#float

	#need str method?
	#need class Meta?