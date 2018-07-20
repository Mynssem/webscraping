#Vários tipos de Web Scraping
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime
import re

pages=set()
random.seed(datetime.datetime.now())

#Recupera uma lista de todos os links internos encontrados em uma página
def getInternalLinks(bsObj, includeUrl):
	internalLinks=[]
	#Encontra todos os links que começam com "/"
	for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] not in internalLinks:
				internalLinks.append(link.attrs['href'])
	return internalLinks
#Recupera uma lista de todos os links externos encontrados em uma página
def getExternalLinks(bsObj,excludeUrl):
	externalLinks=[]
	#Encontra todos os links que começam com "http" ou "www" que não contem o URL atual
	for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
		if link.attrs['href'] is not None:
			if link.attrs['href'] is not externalLinks:
				externalLinks.append(link.attrs['href'])
	return externalLinks

def splitAddress(address):
	addressParts = address.replace("http://", " ").split("/")
	return addressParts

def getRandomExternalLink(startingPage):
	html=urlopen(startingPage)
	bsObj=BeautifulSoup(html)
	externalLinks=getInternalLinks(bsObj, splitAddress(startingPage)[0])
	if len(externalLinks)==0:
		internalLinks=getInternalLinks(startingPage)
		return getEXternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])

	else:
		return externalLinks[random.randint(0, len(externalLinks)-1)]

def followExternalOnly(startingSite):
	externalLink=getRandomExternalLink("http://oreilly.com")
	print("random external link is: "+externalLink)
	followExternalOnly(externalLink)

followExternalOnly("http://oreilly.com")
