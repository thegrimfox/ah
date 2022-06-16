
html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names
were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

 # RESOLUCION.
print("\n*** Ahora se mostrara el codigo HTML ***\n")
print(soup.prettify())

print("\nLos links de Elsie, Lacie y Tillie son los siguientes: \n")
for href in soup.find_all('a',href=True):
    print(href.get('href'))

print("\nEl Link correspondiente a la hermana Tillie es: \n")
print(soup.find_all(id="link2"))
