from django.db import models

CARGO_CHOICES = ((1, 'Prefeito'),)


class Pessoa(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    doc = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return "{} - {}".format(self.nome, self.doc)

    def nome_formatado(self):
        return self.nome.replace(' ','+')


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    doc = models.CharField(max_length=100, unique=True)
    doc_raiz = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "{} - {}".format(self.razao_social, self.doc_raiz)


class Sociedade(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    tipo_socio = models.CharField(max_length=100)
    qualificacao_socio = models.CharField(max_length=100)

    def __str__(self):
        return "{} ({})".format(self.empresa, self.pessoa)


class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.IntegerField(choices=CARGO_CHOICES)
    numero = models.IntegerField()
    partido = models.CharField(max_length=8)
    id = models.BigIntegerField(primary_key=True)

    def __str__(self):
        return "{} - {}".format(self.nome, str(self.numero))


class Receita(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, verbose_name="Candidato")
    pessoa_doador = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Doador")
    doc_originario = models.CharField(max_length=16, null=True)
    nome_doador_originario = models.CharField(max_length=100, null=True)
    data = models.DateField()
    especia_do_recurso = models.CharField(max_length=100)
    descricao_do_recurso = models.CharField(max_length=200, null=True, verbose_name="Descrição do recurso")
    numero_documento = models.CharField(max_length=100, null=True)
    recibo_eleitoral = models.CharField(max_length=100, null=True)
    valor = models.DecimalField(max_digits=100, decimal_places=2, verbose_name='Valor (R$)')
    fonte = models.CharField(max_length=100)

    def __str__(self):
        return "R$: {}: de {} para {} ".format(self.valor, self.pessoa_doador.nome, str(self.candidato.nome))


class Despesa(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True, verbose_name="Candidato")
    doc_fornecedor = models.CharField(max_length=16)
    nome_fornecedor = models.CharField(max_length=100, null=True, verbose_name="Fornecedor")
    doc_doador_originario = models.CharField(max_length=16, null=True)
    nome_doador_originario = models.CharField(max_length=100, null=True)
    data = models.DateField()
    especia_do_recurso = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=100, null=True)
    recibo_eleitoral = models.CharField(max_length=100, null=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Valor (R$)')

    def __str__(self):
        return "{} - {}".format(self.candidato, str(self.valor))







