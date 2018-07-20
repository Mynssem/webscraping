#Scraper que coleta o título, o primeiro parágrafo do conteúdo e o 
#link para edição da página
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import re

pages=set()

def getLinks(pageUrl):
	global pages
	html=urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj=BeautifulSoup(html,"lxml")
	try:
		print(bsObj.h1.get_text())
		print(bsObj.find(id="mw-content-text").findAll("p")[0])
		print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
	except AttributeError:
		print("This page is missing something! No worries though!")

	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				#Encontramos uma nova página
				newPage=link.attrs['href']
				print("----------------\n"+newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")
