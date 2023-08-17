import requests

from lxml import etree
from bs4 import BeautifulSoup


link = 'https://www.kabum.com.br/hardware'


webpage = requests.get(link, timeout=10)
soup = BeautifulSoup(webpage.content, 'html.parser')

informacao_pagamento = soup.find_all('div', class_='sc-3b515ca1-0 gyJsdF availablePricesCard')

produtos = soup.find_all('div', class_='sc-d55b419d-11 hJDLPs')


for produto in produtos:
    titulo = produto.find_all('div')[0].find('span').text
    preco_antigo = produto.find_all('div')[1].find_all('span')[0].text
    preco_novo = produto.find_all('div')[1].find_all('span')[1].text
    metodo = produto.find_all('div')[1].find_all('span')[2].text

    print(f'De {preco_antigo} por {preco_novo} {metodo}')

  
