#exemplo de scraping que utiliza a função next_sibling -> facilita a coleta de dados em tabelas, principalmente as que tem linhas de títulos 
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
	print(sibling)	

