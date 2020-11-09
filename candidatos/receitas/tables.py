import django_tables2 as tables
from .models import Receita, Despesa

class ReceitaTable(tables.Table):
    class Meta:
        model = Receita
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("candidato", "nome_doador", "valor", "descricao_do_recurso")

class DespesaTable(tables.Table):
    class Meta:
        model = Despesa
        template_name = "django_tables2/bootstrap-responsive.html"
        fields = ("candidato", "nome_fornecedor", "valor")