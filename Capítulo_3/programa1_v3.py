#Versão mais completa do programa de captura de links do Wikipedia
#Nele, o usuário entra com uma URL da forma /wiki/<nome_do_artigo>, o programa retorna um link aleatório associado ao artigo
#E dentro deste link aleatório o processo continua indeterminadamente

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime #para os números pseudo aleatórios
import random
import re

random.seed(datetime.datetime.now()) #atualiza os números pseudoaleatórios em cada uso

def getLinks(articleUrl):
	html=urlopen("http://en.wikipedia.org"+articleUrl)
	bsObj=BeautifulSoup(html,"lxml")
	return bsObj.find("div",{"id": "bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links=getLinks("/wiki/Kevin_Bacon")

while len(links)>0:
	newArticle=links[random.randint(0, len(links)-1)].attrs["href"]
	print(newArticle)
	links=getLinks(newArticle)
