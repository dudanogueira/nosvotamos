# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle
import os
import datetime
import time

from materias.models import Materia

total_paginas = 1 # 160
paginas = range(1,total_paginas+1)


class ParseUrlMateria(object):

    def __init__(self, url):
        print("ENTROU PARSE: ", url)
        self.retorno = {}
        id = url.split("=")[1]
        self.retorno['id'] = id
        self.retorno['url'] = url
        time.sleep(3)
        conteudo = urlopen(url).read()
        self.soup = BeautifulSoup(conteudo, 'html.parser')
        self.tds = self.soup.find_all("td")

    def parse(self):
        print(self.retorno)

class Command(BaseCommand):
    help = "Importa Materias de Teofilo Otoni"

    # def add_arguments(self, parser):
    #     pass
    #     #parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        links_bruto = []
        for pagina in paginas:
            pagina_url = 'http://www.camarafoz.pr.gov.br/projetos.php?ordem=&ni=15&pp=152&pa=%d&palavra=&tipo=' % pagina
            time.sleep(2)
            conteudo = urlopen(pagina_url).read()
            soup = BeautifulSoup(conteudo, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if 'projetos.php?p2=' in link.attrs['href']:
                    links_bruto.append("http://www.camarafoz.pr.gov.br/%s" % link.attrs['href'])
        links_bruto = list(set(links_bruto))
        print(links_bruto)
        for url_materia in links_bruto:
            parser = ParseUrlMateria(url_materia)
            parser.parse()