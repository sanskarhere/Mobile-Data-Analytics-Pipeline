from bs4 import BeautifulSoup
import requests

with open('data/html/mobile.html','r',encoding='UTF-8') as f:
    html=f.read()

soup=BeautifulSoup(html,'lxml')

print(soup.prettify())