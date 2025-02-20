from django.db import models

class Clientes(models.Model):
    idclientes = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=255, blank=True, null=True,help_text="Razão Social ou Nome Completo.")
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True,help_text="Fantasia ou Primeiro Nome.")
    celular = models.CharField(max_length=30, blank=True, null=True,help_text="Celular do cliente.")
    email = models.CharField(max_length=255, blank=True, null=True,help_text="Este campo além do e-mail é utilizado como login do cliente.")
    nome_metatrader = models.CharField(max_length=255, blank=True, null=True,help_text="O sistema compara este nome com o nome retornado pela corretora para o caso de EAs Metatrader, em geral é o nome completo do cliente.")
    senha = models.CharField(max_length=255, blank=True, null=True,help_text="Senha de acesso aos aplicativos Captura e Robô Trader.")
    login_habilitado = models.IntegerField(blank=True, null=True,help_text="1 para clientes cujo login está habilitado nos aplicativos, alguns clientes são apenas terceiros receptores de sinal e não precisam fazer login, porém precisamos ter eles cadastrados na base para vincular nas demais tabelas.")
    ativo = models.IntegerField(blank=True, null=True,help_text="1 para cliente ativo e 0 para cliente inativo.")
    cpf = models.CharField(max_length=20, blank=True, null=True,help_text="CPF para emissão de nota fiscal.")

    def __str__(self):
        return self.razao_social  # Substitua pelo campo desejado

    class Meta:
        managed = False
        verbose_name = "1 - Cadastro de Cliente"
        verbose_name_plural = "1 - Cadastro de Clientes"
        db_table = 'clientes'


############################
############################

#Emissor de Sinal
class SinaisRecebidos(models.Model):

    OPÇÕES_ARREDONDAMENTO = [
        (1, "ROUND_HALF_DOWN"),
        (2, "ROUND_HALF_UP"),
        (3, "ROUND_HALF_EVEN"),
        (4, "ROUND_UP"),
        (5, "ROUND_DOWN"),
    ]

    ATIVOS = [
        ("WIN", "WIN"),
        ("WDO", "WDO"),
    ]

    idsinais_recebidos = models.AutoField(primary_key=True)
    nome_sinal = models.CharField(max_length=200, blank=True, null=True,verbose_name="Nome do Sinal",help_text="Insira o nome completo do usuário.")
    conta = models.CharField(max_length=45, blank=True, null=True, verbose_name="Conta",help_text="Preencha o número da conta do emissor de sinal.")
    sigla_ativo = models.CharField(choices=ATIVOS, max_length=10, blank=True, null=True, verbose_name="Ativo")
    divisor_sinal = models.DecimalField(max_digits=7, decimal_places=3)
    qtde_maxima_contratos = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    stop_financeiro_maximo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    id_sinais_monitoramento_stop = models.CharField(max_length=20, blank=True, null=True)
    margem_necessaria = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    idclientes = models.IntegerField()
    idarredondamento = models.IntegerField(choices=OPÇÕES_ARREDONDAMENTO, default=1, verbose_name="Tipo de Arredondamento")  # Dropdown fixo
    qtd_digitos_decimais = models.PositiveIntegerField(verbose_name="Digitos Decimais")
    ativo = models.IntegerField()
    nome_emissor = models.CharField(max_length=45, blank=True, null=True)
    monitorar_emissor = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome_sinal

    class Meta:
        managed = False
        verbose_name = "2 - Cadastro de Emissor"
        verbose_name_plural = "2 - Cadastro de Emissores"
        db_table = 'sinais_recebidos'
        unique_together = (('sigla_ativo', 'conta', 'divisor_sinal'),)


############################
############################

#Rececptor de Sinal
class ClientesSinais(models.Model):


    EA = [
        ("EA6", "EA6"),
        ("Captura", "Captura"),
    ]

    SIM_NAO = [
        (1, "SIM"),
        (0, "NÃO"),
    ]

    idclientes_sinais = models.AutoField(primary_key=True)
    idclientes = models.PositiveIntegerField()
    idportifolio = models.PositiveIntegerField()
    multiplicador = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True,
                                        help_text="Valor inteiro pelo qual o sinal emissor será multiplicado neste receptor. Ex: (1,5 ou 10)")
    numero_conta = models.CharField(max_length=30, blank=True, null=True,
                                    verbose_name="Número da Conta",
                                    help_text="Número da conta receptora deste sinal.")
    senha_conta = models.CharField(max_length=30, blank=True, null=True,
                                    verbose_name="Senha da Conta Metatrader",
                                    help_text="Senha da conta receptora do sinal. Só preencher este campo se o receptor for Metatrader/EA6.")

    nome_ea = models.CharField(choices=EA, max_length=50, blank=True, null=True,verbose_name="Software Receptor")
    magic_number = models.PositiveIntegerField(blank=True, null=True,
                                               verbose_name="Magic Number",
                                               help_text="Identificador do Robô. Só preencher este campo se o receptor for Metatrader/EA6.")
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ativo = models.IntegerField()
    idsinais_recebidos = models.PositiveIntegerField(verbose_name="Emissor de Sinal")
    tipo_sinal = models.IntegerField()
    utilizar_mesmo_ativo_sinal = models.IntegerField(choices=SIM_NAO,blank=True, null=True,
                                                     verbose_name="Utilizar o mesmo Ativo do Emissor",
                                                     help_text="Só preencher este campo se o receptor for Metatrader/EA6.")

    sigla_ativo_cliente = models.CharField(max_length=45, blank=True, null=True,
                                               verbose_name="Codigo do Ativo no Receptor",
                                               help_text="Caso a resposta anterior seja NÃO preencha o código. Só preencher este campo se o receptor for Metatrader/EA6.")

    corretora = models.CharField(max_length=45, blank=True, null=True,
                                               help_text="Corretora na qual o Metatrader foi contratado.")

    cliente_logado = models.IntegerField(blank=True, null=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    idmetatrader_servidores = models.PositiveIntegerField(blank=True, null=True)
    posicao_atual = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    data_posicao = models.DateTimeField(blank=True, null=True)
    monitorar_receptor = models.IntegerField(blank=True, null=True)
    saldo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    capital_liquido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome_ea  # Substitua pelo campo desejado

    class Meta:
        managed = False
        verbose_name = "3 - Cadastro de Receptor"
        verbose_name_plural = "3 - Cadastro de Receptores"
        db_table = 'clientes_sinais'


############################
############################

#Historico de Operações
class MetatraderHistorico(models.Model):
    idmetatrader_historico = models.BigAutoField(primary_key=True)
    idclientes = models.PositiveIntegerField()
    idmetatrader_servidores = models.ForeignKey('MetatraderServidores', models.DO_NOTHING, db_column='idmetatrader_servidores')
    numero_conta = models.PositiveIntegerField()
    data_transacao = models.DateTimeField()
    sigla_ativo = models.CharField(max_length=255)
    oferta = models.PositiveBigIntegerField()
    ordem = models.PositiveBigIntegerField()
    posicao = models.PositiveBigIntegerField()
    tipo = models.IntegerField()
    direcao = models.IntegerField()
    volume = models.FloatField()
    preco = models.FloatField()
    custo = models.FloatField()
    sl = models.FloatField()
    tp = models.FloatField()
    comissao = models.FloatField()
    taxa = models.FloatField()
    swap = models.FloatField()
    lucro = models.FloatField()
    mudanca = models.FloatField()
    id_ea = models.PositiveBigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    transacao_fechada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        verbose_name = "4 - Historico de Operações"
        verbose_name_plural = "4 - Historico de Operações"
        db_table = 'metatrader_historico'

############################
############################

class MetatraderServidores(models.Model):
    idmetatrader_servidores = models.AutoField(primary_key=True)
    nome_servidor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'metatrader_servidores'