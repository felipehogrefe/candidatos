from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os, time

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'candidatos.settings')
django.setup()

from receitas.models import Pessoa, Empresa, Sociedade


cur_path = os.path.abspath(os.getcwd())
csvs_path = cur_path + '/csvs/socios'


def main():
    for pessoa in Pessoa.objects.all():
        print(pessoa.nome)
        recupera_dados_empresas(pessoa)


def processa_csvs(pessoa):
    for csv in os.listdir(csvs_path):
        file = open(csvs_path + '/' + csv, encoding="utf-8")
        for line in file.readlines()[1:]:
            dados = line.split(',')
            cnpj = dados[0]
            razao_social = dados[1]
            doc_socio = dados[2]
            nome_socio = dados[3]
            tipo_socio = dados[4]
            qualificacao_socio = dados[5]
            try:
                print(pessoa.doc[3:9], doc_socio.replace('*', ''), nome_socio)
                if pessoa.doc[3:9] == doc_socio.replace('*', ''):
                    empresa = Empresa.objects.get_or_create(
                        razao_social=razao_social,
                        doc=cnpj
                    )
                    Sociedade.objects.get_or_create(
                        pessoa=pessoa,
                        empresa=empresa[0],
                        tipo_socio=tipo_socio,
                        qualificacao_socio=qualificacao_socio

                    )
                else:
                    print("CPF não corresponde: {} - {}".format(nome_socio, csv))
            except Exception as e:
                print(e)

        file.close()
        os.remove(csvs_path + '\\' + csv)


def recupera_dados_empresas(pessoa):
    chrome_options = configura_chrome()
    chrome = webdriver.Chrome('chromedriver.exe', options=chrome_options)
    url = "https://brasil.io/dataset/socios-brasil/socios/?search={}&format=csv".format(pessoa.nome_formatado())
    chrome.get(url)
    time.sleep(2)
    processa_csvs(pessoa)


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