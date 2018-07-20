#Este programa seleciona todo o conteúdo de uma página e depois mostra na tela somente o texto que estiver entre as tags:
#<span class="green"></span>
#No exemplo da página utilizada, os textos entre estas tags são nomes

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"lxml")

nameList=bsObj.findAll("span", {"class":"green"})
for name in nameList:
	print(name.get_text())

#Quando usamos name.get_text() removemos as tags e obtemos somente o texto, se quisermos o texto com todas as tags devemos 

