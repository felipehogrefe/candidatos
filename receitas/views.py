from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import register
from django.views import generic
from .models import Candidato, Receita, Despesa, Sociedade, Empresa, Pessoa
from .tables import ReceitaTable, DespesaTable
from django.shortcuts import render, get_object_or_404, reverse
from collections import defaultdict

from django_tables2 import SingleTableView


class ReceitasView(SingleTableView):
    SingleTableView.table_pagination = False
    model = Receita
    table_class = ReceitaTable
    template_name = 'receitas/receitas.html'


class DespesasView(SingleTableView):
    SingleTableView.table_pagination = False
    model = Despesa
    table_class = DespesaTable
    template_name = 'receitas/despesas.html'


class IndexView(generic.TemplateView):
    template_name = 'receitas/index.html'


def pessoa_detail(request, pessoa_id):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    empresas = [sociedade.empresa for sociedade in Sociedade.objects.filter(pessoa=pessoa)]
    return render(request, 'receitas/pessoa_detail.html', {'pessoa_detail': pessoa, 'empresas': empresas})


def get_candidatos(request):

    dados_receita = defaultdict(list)
    for receita in Receita.objects.all():
        sociedades = Sociedade.objects.filter(pessoa=receita.pessoa_doador)
        str_empresas = []
        for sociedade in sociedades:
            if str(sociedade.empresa) not in str_empresas:
                str_empresas.append(str(sociedade.empresa))
        dados_receita[receita.candidato].append(((str_empresas, receita.pessoa_doador), receita.valor))

    for candidato in dados_receita:
        dados_receita[candidato].sort(key=lambda tup: tup[1], reverse=True)
        dados_receita[candidato] = dados_receita[candidato][:10]

    return render(request, 'receitas/candidatos.html', {'dados_receita': dados_receita})

@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict_data.get(key)




