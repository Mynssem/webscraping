#Versão mais completa do programa de captura de links do Wikipedia
#Nele, o usuário entra com uma URL da forma /wiki/<nome_do_artigo> e o programa retorna uma lista das URLs dos artigos vinculados

from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

pages=set()

def getLinks(pageUrl):
	global pages
	html=urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj=BeautifulSoup(html)
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#Encontramos uma nova página
				newPage=link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")
