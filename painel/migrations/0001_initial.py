# Generated by Django 5.0 on 2025-02-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clientes",
            fields=[
                ("idclientes", models.AutoField(primary_key=True, serialize=False)),
                (
                    "razao_social",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "nome_fantasia",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("celular", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "nome_metatrader",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("senha", models.CharField(blank=True, max_length=255, null=True)),
                ("login_habilitado", models.IntegerField(blank=True, null=True)),
                ("ativo", models.IntegerField(blank=True, null=True)),
                ("cpf", models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                "verbose_name": "Cliemte",
                "verbose_name_plural": "Clientes",
                "db_table": "clientes",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="ClientesSinais",
            fields=[
                (
                    "idclientes_sinais",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("idclientes", models.PositiveIntegerField()),
                ("idportifolio", models.PositiveIntegerField()),
                (
                    "multiplicador",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=9, null=True
                    ),
                ),
                (
                    "numero_conta",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                ("senha_conta", models.CharField(blank=True, max_length=30, null=True)),
                ("nome_ea", models.CharField(blank=True, max_length=50, null=True)),
                ("magic_number", models.PositiveIntegerField(blank=True, null=True)),
                ("data_cadastro", models.DateTimeField(blank=True, null=True)),
                ("ativo", models.IntegerField()),
                ("idsinais_recebidos", models.PositiveIntegerField()),
                ("tipo_sinal", models.IntegerField()),
                (
                    "utilizar_mesmo_ativo_sinal",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "sigla_ativo_cliente",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("corretora", models.CharField(blank=True, max_length=45, null=True)),
                ("cliente_logado", models.IntegerField(blank=True, null=True)),
                ("ultimo_login", models.DateTimeField(blank=True, null=True)),
                (
                    "idmetatrader_servidores",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                (
                    "posicao_atual",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=9, null=True
                    ),
                ),
                ("data_posicao", models.DateTimeField(blank=True, null=True)),
                ("monitorar_receptor", models.IntegerField(blank=True, null=True)),
                (
                    "saldo",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                (
                    "capital_liquido",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=14, null=True
                    ),
                ),
                ("online", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Receptor",
                "verbose_name_plural": "Receptores",
                "db_table": "clientes_sinais",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MetatraderHistorico",
            fields=[
                (
                    "idmetatrader_historico",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("idclientes", models.PositiveIntegerField()),
                ("numero_conta", models.PositiveIntegerField()),
                ("data_transacao", models.DateTimeField()),
                ("sigla_ativo", models.CharField(max_length=255)),
                ("oferta", models.PositiveBigIntegerField()),
                ("ordem", models.PositiveBigIntegerField()),
                ("posicao", models.PositiveBigIntegerField()),
                ("tipo", models.IntegerField()),
                ("direcao", models.IntegerField()),
                ("volume", models.FloatField()),
                ("preco", models.FloatField()),
                ("custo", models.FloatField()),
                ("sl", models.FloatField()),
                ("tp", models.FloatField()),
                ("comissao", models.FloatField()),
                ("taxa", models.FloatField()),
                ("swap", models.FloatField()),
                ("lucro", models.FloatField()),
                ("mudanca", models.FloatField()),
                ("id_ea", models.PositiveBigIntegerField()),
                ("comentario", models.CharField(blank=True, max_length=255, null=True)),
                ("transacao_fechada", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Historico",
                "verbose_name_plural": "Historico",
                "db_table": "metatrader_historico",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="MetatraderServidores",
            fields=[
                (
                    "idmetatrader_servidores",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("nome_servidor", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "metatrader_servidores",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SinaisRecebidos",
            fields=[
                (
                    "idsinais_recebidos",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("nome_sinal", models.CharField(blank=True, max_length=200, null=True)),
                ("conta", models.CharField(blank=True, max_length=45, null=True)),
                ("sigla_ativo", models.CharField(blank=True, max_length=10, null=True)),
                ("divisor_sinal", models.DecimalField(decimal_places=3, max_digits=7)),
                (
                    "qtde_maxima_contratos",
                    models.DecimalField(
                        blank=True, decimal_places=3, max_digits=6, null=True
                    ),
                ),
                (
                    "stop_financeiro_maximo",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                (
                    "id_sinais_monitoramento_stop",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "margem_necessaria",
                    models.DecimalField(
                        blank=True, decimal_places=0, max_digits=6, null=True
                    ),
                ),
                ("idclientes", models.IntegerField()),
                (
                    "idarredondamento",
                    models.IntegerField(
                        choices=[
                            (1, "ROUND_HALF_DOWN"),
                            (2, "ROUND_HALF_UP"),
                            (3, "ROUND_HALF_EVEN"),
                            (4, "ROUND_UP"),
                            (5, "ROUND_DOWN"),
                        ],
                        default=1,
                        verbose_name="Tipo de Arredondamento",
                    ),
                ),
                (
                    "qtd_digitos_decimais",
                    models.PositiveIntegerField(verbose_name="Digitos Decimais"),
                ),
                ("ativo", models.IntegerField()),
                (
                    "nome_emissor",
                    models.CharField(blank=True, max_length=45, null=True),
                ),
                ("monitorar_emissor", models.IntegerField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Emissor",
                "verbose_name_plural": "Emissores",
                "db_table": "sinais_recebidos",
                "managed": False,
            },
        ),
    ]
