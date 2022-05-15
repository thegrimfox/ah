from bs4 import BeautifulSoup

html_doc = """ <html><head><tittle>the dormouse's story</tittle></head>
<body>
<p class="tittle"><b>the dormouse's story</b></p>

<p class="story">once upen a time there were three little sisters; and their names weres
<a href="http://example.com/elsie" class="sister" id="link1>Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2>Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3>Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
