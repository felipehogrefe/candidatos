# Generated by Django 3.1.3 on 2020-11-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='numero_documento',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='recibo_eleitoral',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='receita',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Valor (R$)'),
        ),
    ]