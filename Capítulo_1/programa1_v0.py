#Programa simples - somente leitura de uma página sem nenhum tipo de organização de dados
from urllib.request import urlopen
html=urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())
