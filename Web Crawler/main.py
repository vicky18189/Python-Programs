
from turtle import clear, title
from bs4 import BeautifulSoup
import requests

def web_scrape():

    url = 'https://stackoverflow.com/questions/'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for link in soup.findAll('a', {'class': 'question-hyperlink'}):
        href = link.get('href')
        title = link.string
        if href is not None:
            print(title +'('+href+')')
            
clear
web_scrape()
