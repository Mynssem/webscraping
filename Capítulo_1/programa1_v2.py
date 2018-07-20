#Nosso scraping agora estará preparado caso aconteça algum problema na página requisitada
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
if html is None:
	print("URL is not found")
	#retorna null, break ou executa algum outro "plano B"
else:
	#o programa continua.
	bsObj = BeautifulSoup(html.read(),"lxml");
	print(bsObj.h1)

