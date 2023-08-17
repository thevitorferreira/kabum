import requests

from bs4 import BeautifulSoup

def make_request(link, retries=0):
    print(link)
    try:
        webpage = requests.get(link)
        soup = BeautifulSoup(webpage.content, 'html.parser')
        return(soup)


    except: 
        print('Erro')