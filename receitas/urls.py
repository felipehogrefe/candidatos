from django.urls import path

from . import views

app_name = 'receitas'
urlpatterns = [
    path('lista_receitas/', views.ReceitasView.as_view(), name='receitas'),
    path('lista_despesas/', views.DespesasView.as_view(), name='despesas'),
    path('candidatos/', views.get_candidatos, name='candidatos'),
    path('pessoas/<int:pessoa_id>/', views.pessoa_detail, name='pessoa_detail'),
    path('', views.IndexView.as_view(), name='index'),
]