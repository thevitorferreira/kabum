import pandas as pd
from src.infra.request.request import make_request
from src.application.services.produtos.get_produtos import GetProdutos

class GetTodasPaginas():

    def __init__(self, df_categorias):
        self._df_categorias = df_categorias

    def get_todas_paginas(self):
        for col, row in self._df_categorias.iterrows():
            print(f'----->{row["nome_categoria"]}<-----')
            link = row['link'] + '?page_number=1&page_size=100&facet_filters=&sort=most_searched'
            soup = make_request(link)
            lista_de_indices = soup.find_all('a', class_='page')
            for pagina in lista_de_indices:
                pagina_final = pagina.text
            teste = GetProdutos(pagina_final).get_produtos(row['link'], row['nome_categoria'])

            