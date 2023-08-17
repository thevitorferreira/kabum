import pandas as pd
from src.infra.request.request import make_request


class GetTodasPaginas():

    def __init__(self, df_categorias):
        self._df_categorias = df_categorias

    def get_todas_paginas(self):
        print('chegou')
        for col, row in self._df_categorias.iterrows():
            link = row['link'] + '?page_number=1&page_size=100&facet_filters=&sort=most_searched'
            soup = make_request(link)
            lista_de_indices = soup.find_all('a', class_='page')
            print(lista_de_indices)
            for pagina in lista_de_indices:
                pagina_final = pagina.text
            print(pagina_final)