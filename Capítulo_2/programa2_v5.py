#Scrapy que obtém todos os caminhos das imagens de um site (sem contar a logo)
from urllib.request import urlopen

from bs4 import BeautifulSoup
import re
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")
images = bsObj.findAll("img", {"src":re.compile("\.\./img\/gifts/img.*\.jpg")})


for image in images:
	print(image["src"])
