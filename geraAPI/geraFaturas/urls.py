from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^distribuidoras/$', views.DistribuidoraList.as_view(), name='distribuidora-list'),
	url(r'^distribuidora/(?P<pk>[0-9]+)/$', views.DistribuidoraDetail.as_view(), name='distribuidora-detail'),

    url(r'^clientes/$', views.ClienteList.as_view(), name='cliente-list'),
	url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view(), name='cliente-detail'),


	# Implementar endpoint com listagem de nomes de Clientes, informando suas respectivas
	# Distribuidoras e os valores médio, máximo e mínimo de Faturas.
	url(r'^clientesInfo/$', views.ClienteListInfo.as_view(), name='cliente-list-info'),

	url(r'^faturas/$', views.FaturaList.as_view(), name='fatura-list'),
	url(r'^fatura/(?P<pk>[0-9]+)/$', views.FaturaDetail.as_view(), name='fatura-detail'),

	


 


]
