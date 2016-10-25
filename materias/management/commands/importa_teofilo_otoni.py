# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle
import os
import datetime
import time

from materias.models import Materia

total_paginas = 5
paginas = range(1,total_paginas+1)
links_bruto = []

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
        for td in self.tds:
            if td.b:
                if "Tipo" in td.b.string:
                    self.retorno['tipo'] = td.contents[1].split('-')[0].replace('\n','').strip()
                if u"Número" in td.b.string:
                    self.retorno['numero_referencia'] = td.contents[1].split('-')[0].replace('\n','').strip()
                    self.retorno['numero'] = self.retorno['numero_referencia'].split('/')[0]
                    self.retorno['ano'] = self.retorno['numero_referencia'].split('/')[1]
                if "Data" in td.b.string:
                    data_str = td.contents[1].split('-')[0].replace('\n','').strip()
                    self.retorno['data'] = data_str
                if "Ementa" in td.b.string:
                    ementa = td.contents[1].replace('\n','').strip()
                    self.retorno['ementa'] = ementa
                if "Autor" in td.b.string:
                    autor = td.contents[2].strip()
                    if autor:
                        self.retorno['autor'] = autor
                else:
                    self.retorno['autor'] = 'Autoria Desconhecida'
                if td.find('a'):
                    self.retorno['url_materia_integra'] = td.find('a').attrs['href']
                else:
                    self.retorno['url_materia_integra'] = ''
                if u"Em Tramitação" in td.b.string:
                    if u"Não" in td.contents[1].strip():
                        tramita = False
                    else:
                        tramita = True
                    self.retorno['tramita'] = tramita
                if u"Polêmica" in td.b.string:
                    if u"Não" in td.contents[1].strip() or td.contents[1].strip() == '':
                        polemica = False
                    else:
                        polemica = True
                    self.retorno['polemica'] = tramita
                if u"Regime" in td.b.string:
                    regime = td.contents[1].strip()
                    self.retorno['regime'] = regime

class Command(BaseCommand):
    help = "Importa Materias de Teofilo Otoni"

    # def add_arguments(self, parser):
    #     pass
    #     #parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        thefile = open('links_brutos.p', 'w')
        for pagina in paginas:
            pagina_url = 'http://sapl.teofilootoni.mg.leg.br/generico/materia_pesquisar_proc?page=%d&step=8&txt_relator=&txt_numero=&dt_public2=&lst_tip_autor=&txt_num_protocolo=&hdn_txt_autor=&txt_ano=&rd_ordem_td=1&dat_sessao=00/00/0000&hdn_cod_autor=&lst_localizacao=&lst_tip_materia=&txt_assunto=&btn_materia_pesquisar=Pesquisar&incluir=0&rd_ordenacao=2&dt_apres2=&lst_cod_partido=&chk_coautor=&lst_status=&dt_public=&rad_tramitando=&total_materias=901&txt_npc=&existe_ocorrencia=0&dt_apres=' % pagina
            time.sleep(2)
            conteudo = urlopen(pagina_url).read()
            soup = BeautifulSoup(conteudo, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                if 'materia_mostrar_proc?' in link.attrs['href']:
                    links_bruto.append(link.attrs['href'])
            # escreve arquivo com links brutos
            #pickle.dump(links_bruto, thefile)
        for url_materia in links_bruto:
            parser = ParseUrlMateria(url_materia)
            parser.parse()
            materia_dict = parser.retorno
            materia,created = Materia.objects.get_or_create(
                id_referencia=materia_dict['id'],
                ano=materia_dict['ano'],
            )
            materia.autor = materia_dict['autor'] or None
            materia.data = datetime.datetime.strptime(materia_dict['data'], '%d/%m/%Y')
            materia.ementa = materia_dict['ementa']
            materia.numero = materia_dict['numero']
            materia.numero_referencia = materia_dict['numero_referencia']
            materia.polemica = materia_dict['polemica']
            materia.regime = materia_dict['regime']
            materia.tramita = materia_dict['tramita']
            materia.url = materia_dict['url']
            materia.url_materia_integra = materia_dict['url_materia_integra']
            materia.tipo = materia_dict['tipo']
            materia.dados = materia_dict
            materia.save()
