from src.configuration import KABUMLINKS
from src.application.services.categories.get_categories import GetCategories
from src.application.services.categories.get_todas_paginas import GetTodasPaginas


def run():
    categorias = GetCategories(
        KABUMLINKS['base_link'] + KABUMLINKS['hardware_page_link'])
    df_categorias = categorias.get_categories()
    print(df_categorias)

    todas_paginas = GetTodasPaginas(df_categorias)
    todas_paginas.get_todas_paginas()

