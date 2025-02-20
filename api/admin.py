from django.contrib import admin
from .models import Clientes,SinaisRecebidos,ClientesSinais,MetatraderHistorico
from django import forms

@admin.register(Clientes)
class Clientes_Admin(admin.ModelAdmin):
    list_display = ('razao_social', 'nome_fantasia', 'celular', 'email', 'login_habilitado')
    search_fields = ('idclientes',)

@admin.register(SinaisRecebidos)
class SinaisRecebidos_Admin(admin.ModelAdmin):
    list_display = ('nome_sinal', 'conta', 'sigla_ativo', 'divisor_sinal', 'qtde_maxima_contratos','qtd_digitos_decimais')
    search_fields = ('idsinais_recebidos',)

@admin.register(ClientesSinais)
class ClientesSinais_Admin(admin.ModelAdmin):
    list_display = ('idclientes', 'multiplicador', 'numero_conta', 'nome_ea', 'data_cadastro')
    search_fields = ('idclientes',)

@admin.register(MetatraderHistorico)
class MetatraderHistorico_Admin(admin.ModelAdmin):
    fields = ('numero_conta', 'data_transacao','sigla_ativo', 'oferta', 'ordem', 'posicao', 'tipo','id_ea','transacao_fechada')
    list_display = ('numero_conta', 'data_transacao','sigla_ativo', 'oferta', 'ordem', 'posicao', 'tipo','id_ea','transacao_fechada')
    search_fields = ('idclientes',)
