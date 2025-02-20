from django.contrib import admin
from .models import SinaisRecebidos,ClientesSinais,MetatraderHistorico
from django import forms

#HistoricoResultados
@admin.register(MetatraderHistorico)
class MetatraderHistorico_Admin(admin.ModelAdmin):
    fields = ('numero_conta', 'data_transacao','sigla_ativo', 'oferta', 'ordem', 'posicao', 'tipo','id_ea','transacao_fechada')
    list_display = ('numero_conta', 'data_transacao','sigla_ativo', 'oferta', 'ordem', 'posicao', 'tipo','id_ea','transacao_fechada')
    search_fields = ('idclientes',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(idclientes=request.user.id)

#Emissor de Sinal
@admin.register(SinaisRecebidos)
class SinaisRecebidos_Admin(admin.ModelAdmin):
    list_display = ('idsinais_recebidos','nome_sinal','conta', 'sigla_ativo', 'divisor_sinal')
    #list_editable = ('divisor_sinal',)
    fields = ('nome_sinal', 'conta', 'sigla_ativo', 'divisor_sinal')
    search_fields = ('nome_sinal','conta','sigla_ativo','divisor_sinal',)
    exclude = ('idclientes','ativo','id_sinais_monitoramento_stop',
               'monitorar_emissor','stop_financeiro_maximo',
               'margem_necessaria','idarredondamento','qtd_digitos_decimais',
               'qtde_maxima_contratos','nome_emissor')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Se for um novo registro
            obj.idclientes = request.user.id
            obj.qtde_maxima_contratos = 999
            obj.qtd_digitos_decimais = 0
            obj.ativo = 1
        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(idclientes=request.user.id)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Define o valor inicial de qtd_digitos_decimais como 0
        form.base_fields['divisor_sinal'].initial = 1
        return form

#Receptor de Sinal
@admin.register(ClientesSinais)
class ClientesSinais_Admin(admin.ModelAdmin):
    list_display = ('idsinais_recebidos', 'multiplicador', 'numero_conta', 'nome_ea', 'magic_number', 'utilizar_mesmo_ativo_sinal', 'sigla_ativo_cliente',
              'senha_conta', 'corretora')
    fields = ('idsinais_recebidos', 'multiplicador', 'numero_conta', 'nome_ea', 'magic_number', 'utilizar_mesmo_ativo_sinal', 'sigla_ativo_cliente',
              'senha_conta', 'corretora')
    search_fields = ('nome_ea',)
    exclude = ('idclientes_sinais','idportifolio','idclientes','data_cadastro','ativo','tipo_sinal','cliente_logado','ultimo_login',
               'idmetatrader_servidores','posicao_atual','data_posicao','monitorar_receptor','saldo','capital_liquido','online')


    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Se for um novo registro
            obj.idclientes = request.user.id
            obj.idportifolio = 0
            obj.tipo_sinal = 0
            obj.ativo = 1

        obj.save()

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(idclientes=request.user.id)


    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        user_id = request.user.id
        #sinais_recebidos_choices = SinaisRecebidos.objects.filter(idclientes=user_id)
        sinais_recebidos_choices = SinaisRecebidos.objects.filter(idclientes=user_id).values_list("idsinais_recebidos",flat=True)

        form.base_fields['idsinais_recebidos'] = forms.ModelChoiceField(
            queryset=sinais_recebidos_choices,
            empty_label="Escolha Emissor",
            required=True,
            label = "Nome do Emissor de Sinal"
        )
        # Personaliza o rótulo exibido no combobox
        #form.base_fields['idsinais_recebidos'].label_from_instance = lambda obj: obj.nome_sinal

        return form




