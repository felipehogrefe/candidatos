from django.contrib import admin
from .models import Candidato, Receita, Pessoa, Despesa, Empresa, Sociedade


class CandidatoAdmin(admin.ModelAdmin):
    order_by = ['nome', ]


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('candidato', 'pessoa_doador', 'valor', 'descricao_do_recurso')


class PessoaAdmin(admin.ModelAdmin):
    list_filter = ('nome', 'doc')


class DespesaAdmin(admin.ModelAdmin):
    pass


class EmpresaAdmin(admin.ModelAdmin):
    list_filter = ('razao_social', 'doc')


class SociedadeAdmin(admin.ModelAdmin):
    list_filter = ('pessoa', 'empresa')


admin.site.register(Sociedade, SociedadeAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Receita, ReceitaAdmin)
admin.site.register(Pessoa, PessoaAdmin)