# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Arredondamento(models.Model):
    idarredondamento = models.IntegerField(primary_key=True)
    nome_arredondamento = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'arredondamento'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Clientes(models.Model):
    idclientes = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=255, blank=True, null=True)
    nome_fantasia = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    nome_metatrader = models.CharField(max_length=255, blank=True, null=True)
    senha = models.CharField(max_length=255, blank=True, null=True)
    login_habilitado = models.IntegerField(blank=True, null=True)
    ativo = models.IntegerField(blank=True, null=True)
    cpf = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class ClientesSinais(models.Model):
    idclientes_sinais = models.AutoField(primary_key=True)
    idclientes = models.PositiveIntegerField()
    idportifolio = models.PositiveIntegerField()
    multiplicador = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    numero_conta = models.CharField(max_length=30, blank=True, null=True)
    senha_conta = models.CharField(max_length=30, blank=True, null=True)
    nome_ea = models.CharField(max_length=50, blank=True, null=True)
    magic_number = models.PositiveIntegerField(blank=True, null=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    ativo = models.IntegerField()
    idsinais_recebidos = models.PositiveIntegerField()
    tipo_sinal = models.IntegerField()
    utilizar_mesmo_ativo_sinal = models.IntegerField(blank=True, null=True)
    sigla_ativo_cliente = models.CharField(max_length=45, blank=True, null=True)
    corretora = models.CharField(max_length=45, blank=True, null=True)
    cliente_logado = models.IntegerField(blank=True, null=True)
    ultimo_login = models.DateTimeField(blank=True, null=True)
    idmetatrader_servidores = models.PositiveIntegerField(blank=True, null=True)
    posicao_atual = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    data_posicao = models.DateTimeField(blank=True, null=True)
    monitorar_receptor = models.IntegerField(blank=True, null=True)
    saldo = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    capital_liquido = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_sinais'


class ClientesSinaisConexoes(models.Model):
    idclientes_sinais_conexoes = models.AutoField(primary_key=True)
    data_conexao = models.DateTimeField(blank=True, null=True)
    idclientes_sinais = models.PositiveIntegerField()
    tipo = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_sinais_conexoes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mensagens(models.Model):
    idmensagens = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField(blank=True, null=True)
    data_hora_envio = models.DateTimeField(blank=True, null=True)
    origem_detalhe = models.CharField(max_length=100, blank=True, null=True)
    texto_mensagem = models.CharField(max_length=255, blank=True, null=True)
    enviada = models.IntegerField(blank=True, null=True)
    idmensagens_origem = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'mensagens'


class MensagensOrigem(models.Model):
    idmensagens_origem = models.AutoField(primary_key=True)
    origem = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagens_origem'


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
        db_table = 'metatrader_historico'


class MetatraderServidores(models.Model):
    idmetatrader_servidores = models.AutoField(primary_key=True)
    nome_servidor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'metatrader_servidores'


class Portifolio(models.Model):
    idportifolio = models.AutoField(primary_key=True)
    nome_portifolio = models.CharField(max_length=200, blank=True, null=True)
    portifolio_sigla_ativo = models.CharField(max_length=10)
    margem_necessaria = models.DecimalField(max_digits=6, decimal_places=0)
    ativo = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'portifolio'


class PortifolioItem(models.Model):
    idportifolio_item = models.AutoField(primary_key=True)
    idportifolio = models.PositiveIntegerField()
    idsinais_recebidos = models.PositiveIntegerField()
    multiplicador_sinal = models.DecimalField(max_digits=9, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'portifolio_item'


class PosicoesRecebidas(models.Model):
    idposicoes_recebidas = models.AutoField(primary_key=True)
    data_cadastro = models.DateTimeField()
    idsinais_recebidos = models.IntegerField()
    posicao = models.DecimalField(max_digits=9, decimal_places=3)
    posicao_original = models.DecimalField(max_digits=9, decimal_places=3)
    ativo = models.IntegerField()
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posicoes_recebidas'


class Servidores(models.Model):
    idservidores = models.AutoField(primary_key=True)
    nome_servidor = models.CharField(max_length=200, blank=True, null=True)
    ip_servidor = models.CharField(max_length=50, blank=True, null=True)
    taxa_atualizacao_request = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servidores'


class SinaisRecebidos(models.Model):
    idsinais_recebidos = models.AutoField(primary_key=True)
    nome_sinal = models.CharField(max_length=200, blank=True, null=True)
    conta = models.CharField(max_length=45, blank=True, null=True)
    sigla_ativo = models.CharField(max_length=10, blank=True, null=True)
    divisor_sinal = models.DecimalField(max_digits=7, decimal_places=3)
    qtde_maxima_contratos = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    stop_financeiro_maximo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    id_sinais_monitoramento_stop = models.CharField(max_length=20, blank=True, null=True)
    margem_necessaria = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    idclientes = models.IntegerField()
    idarredondamento = models.PositiveIntegerField()
    qtd_digitos_decimais = models.PositiveIntegerField()
    ativo = models.IntegerField()
    nome_emissor = models.CharField(max_length=45, blank=True, null=True)
    monitorar_emissor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinais_recebidos'
        unique_together = (('sigla_ativo', 'conta', 'divisor_sinal'),)
