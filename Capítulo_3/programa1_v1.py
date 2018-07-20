#Scrapy para capturar todos os links da página do Kevin bacon na Wikipedia
#Este programa servirá como base para os "seis graus de separação"

from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj=BeautifulSoup(html,"lxml")
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])
