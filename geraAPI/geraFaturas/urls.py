from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^distribuidoras/$', views.DistribuidoraList.as_view(), name='distribuidora-list'),
	url(r'^distribuidora/(?P<pk>[0-9]+)/$', views.DitribuidoraDetail.as_view(), name='distribuidora-detail'),

    url(r'^clientes/$', views.ClienteList.as_view(), name='cliente-list'),
	url(r'^cliente/(?P<pk>[0-9]+)/$', views.ClienteDetail.as_view(), name='cliente-detail'),

	url(r'^faturas/$', views.FaturaList.as_view(), name='fatura-list'),
	url(r'^fatura/(?P<pk>[0-9]+)/$', views.FaturaDetail.as_view(), name='fatura-detail'),
]
