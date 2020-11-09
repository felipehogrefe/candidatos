import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'candidatos.settings')
django.setup()

from receitas.models import Candidato, Receita, Despesa, Pessoa

candidato = Candidato.objects.get(pk=20000774385)
candidato.nome = 'ALFREDO GASPAR DE MENDONÇA'
candidato.save()