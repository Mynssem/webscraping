#Primeira utilização do BeautifulSoup
#Este programa ainda muito simples lê uma página da web e imprime o que possuir a tag h1, ou seja, o TÍTULO da página
#Obs: usamos o "lxml" para contornar warnings

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html.read(), "lxml");

print(bsObj.h1)

#A linha de baixo é só um teste para imprimir o texto da página
#print(bsObj.div)
