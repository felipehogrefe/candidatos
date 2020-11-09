import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import logging
import datetime

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'candidatos.settings')
django.setup()

from receitas.models import Candidato, Receita, Despesa, Pessoa

cur_path = os.path.abspath(os.getcwd())
csvs_path = cur_path + '/csvs'
opcoes_csv = ('receitas', 'despesas')

def main():
    # chrome_options = configura_chrome()
    #
    # for candidato in Candidato.objects.all():
    #     for opcao in opcoes_csv:
    #         busca_dados(candidato, opcao, chrome_options)

    processa_dados()


def processa_dados():
    for csv_file in os.listdir(csvs_path):
        file = open(csvs_path+"/"+csv_file, encoding="utf-8")
        nome_candidato = csv_file.split("-")[1]

        if 'Receitas' in csv_file:
            processa_receita(file, nome_candidato)
        elif 'Despesas' in csv_file:
            processa_despesa(file, nome_candidato)

        file.close()


def processa_despesa(file, nome_candidato):
    for line in file.readlines()[1:]:
        data = line.replace('\n', '').split(';')
        Despesa.objects.get_or_create(
            candidato=Candidato.objects.get(nome=nome_candidato),
            doc_fornecedor=data[0],
            nome_fornecedor=data[1].replace('"', ''),
            doc_doador_originario=data[2],
            nome_doador_originario=data[3],
            data=datetime.datetime.fromtimestamp(int(data[4][:10])),
            especia_do_recurso=data[5],
            numero_documento=data[6],
            recibo_eleitoral=data[7],
            valor=round(float(data[8]), 2),
        )


def processa_receita(file, nome_candidato):
    for line in file.readlines()[1:]:
        data = line.replace('\n', '').split(';')
        pessoa = Pessoa.objects.get_or_create(
            nome=data[1].replace('"', ''),
            doc=data[0].replace('"', '')
        )

        Receita.objects.get_or_create(
            candidato=Candidato.objects.get(nome=nome_candidato),
            pessoa_doador=pessoa[0],
            doc_originario=data[2],
            nome_doador_originario=data[3],
            data=datetime.datetime.fromtimestamp(int(data[4][:10])),
            especia_do_recurso=data[5],
            descricao_do_recurso=data[6].replace('"', ''),
            numero_documento=data[7],
            recibo_eleitoral=data[8],
            valor=round(float(data[9]), 2),
            fonte=data[10],
        )


def busca_dados(candidato, opcao, chrome_options):
    chrome = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    url = "https://divulgacandcontas.tse.jus.br/divulga/#/candidato/2020/2030402020/27855/{}/integra/{}".format(
        candidato.id, opcao)
    chrome.get(url)
    element = chrome.find_element_by_link_text('Exportar')
    time.sleep(2)
    chrome.execute_script("arguments[0].click();", element)
    time.sleep(1)
    chrome.close()



def configura_chrome():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--verbose')
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": csvs_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
    })
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-software-rasterizer')
    return chrome_options


if __name__ == '__main__':
    main()


