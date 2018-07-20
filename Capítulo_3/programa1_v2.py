#Scrapy para capturar todos os links da página do Kevin bacon na Wikipedia
#Esta versão é mais completa e seleciona somente os URLs onde o artigo do Kevin Bacon está vinculado e assim, evitaremos links inúteis

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html,"lxml")

for link in bsObj.find("div",{"id": "bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])

#obs: Ao que tudo indica o "if" não é necessário neste código -> a saída é igual
