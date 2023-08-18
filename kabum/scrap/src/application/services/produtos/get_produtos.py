import pandas as pd

from src.configuration import KABUMLINKS
from src.infra.request.request import make_request
from bs4 import BeautifulSoup
import time

class GetProdutos():

    def __init__(self, page):
        self.paginas = int(page)

    def get_produtos(self, link, categoria):

        for i in range(1, self.paginas):
            link_interno = link + f'?page_number={i}&page_size=100&facet_filters=&sort=most_searched'
            soup = make_request(link_interno)
            lista_produtos = soup.find_all('div', class_='sc-d55b419d-11 hJDLPs')
            precos_produto = soup.find_all('div', class_='sc-3b515ca1-0 gyJsdF availablePricesCard')
            count=1

            df_produtos = pd.DataFrame(columns=['nome_produto', 'preco', 'metodo', 'nome_categoria'])
            print(f'PAGINA: {i}')
            for nome,preco in zip(lista_produtos, precos_produto):
                nome_produto = nome.find('div').find('span').text

                precos = preco.find_all('span')
                preco_produto = precos[1].text
                metodo = precos[2].text

                df_produtos = pd.concat([df_produtos, pd.DataFrame(
                data = {'nome_produto': [nome_produto], 'preco' : [preco_produto], 'metodo' : [metodo], 'nome_categoria': [categoria]})], ignore_index=True)
                count+=1

            print(df_produtos)

          
