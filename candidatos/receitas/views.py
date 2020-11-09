from django.http import HttpResponse, HttpResponseRedirect
from django.template.defaultfilters import register
from django.views import generic
from .models import Candidato, Receita, Despesa, Sociedade, Empresa
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


def get_empresas(request):
    dados = defaultdict(list)
    for sociedade in Sociedade.objects.all():
        empresa = sociedade.empresa
        pessoa = sociedade.pessoa
        for receita in Receita.objects.filter(pessoa_doador=pessoa):
            dados[empresa.razao_social].append(receita)
            # dados[empresa.razao_social] = receita.valor if not extra_context[empresa.razao_social][receita.candidato] else extra_context[empresa.razao_social][receita.candidato]+receita.valor

    dados = {}
    for receita in Receita.objects.all():
        empresas = Sociedade.objects.filter(pessoa=receita.pessoa_doador).empresas



    return render(request, 'receitas/empresas.html', {'dados': dados})

@register.filter('get_value_from_dict')
def get_value_from_dict(dict_data, key):
    """
    usage example {{ your_dict|get_value_from_dict:your_key }}
    """
    if key:
        return dict_data.get(key)




