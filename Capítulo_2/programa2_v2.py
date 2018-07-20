#programa para verificar tag "children"
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"lxml")

for child in bsObj.find("table",{"id":"giftList"}).children:
	print(child)

