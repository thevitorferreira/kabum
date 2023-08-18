import pandas as pd
from src.infra.request.request import make_request

class GetCategories:

    def __init__(self, link):
        self._link = link


    def get_categories(self):
        soup = make_request(self._link)

        lista_categorias = soup.find_all('div', class_='sc-dadcc965-4 hiRgJj linkCategoriaListagem')

        dataframe = pd.DataFrame(columns=['link', 'nome_categoria'])

        for categoria in lista_categorias:
            link_categoria = categoria.find('a').get('href')
            nome_categoria = categoria.find('a').text
            dataframe = pd.concat([dataframe, pd.DataFrame(
                data = {'link': [link_categoria], 'nome_categoria' : [nome_categoria]})], ignore_index=True)
            
            print(f'----->{nome_categoria}<-----')
            
        return dataframe
            