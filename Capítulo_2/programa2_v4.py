#Scrapy que  seleciona uma tag, depois seleciona o pai da tag, seleciona o irmão anterior da tg e mostra o texto contido nela
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

