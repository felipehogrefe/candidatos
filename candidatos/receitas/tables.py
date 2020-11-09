import django_tables2 as tables
from .models import Receita, Despesa
from django_tables2.utils import A


class ReceitaTable(tables.Table):
    pessoa_doador = tables.LinkColumn('receitas:pessoa_detail', text=lambda receita: receita.pessoa_doador.nome, args=[A('pk')])
    class Meta:
        model = Receita
        template_name = "receitas/bootstrap.html"
        fields = ("candidato", "pessoa_doador", "valor", "descricao_do_recurso")


class DespesaTable(tables.Table):
    class Meta:
        model = Despesa
        template_name = "receitas/bootstrap.html"
        fields = ("candidato", "nome_fornecedor", "valor")