#Teste simples: LÊ uma página e mostra na tela o Título da página sem as "tags"
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

print(bsObj.h1.get_text())
