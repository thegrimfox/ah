from bs4 import BeautifulSoup
import urllib.request
datos = urllib.request.urlopen('https://www.rutyfirma.com').read().decode()
soup = BeautifulSoup(datos)
tags = soup('a')
for tag in tags:
    print(tag.get('href'))
