import nltk   
from bs4 import *
from urllib import urlopen


url = "http://en.wikipedia.org/wiki/Bradford"
html = urlopen(url).read()
raw = BeautifulSoup(html)
clean_text = raw.get_text().encode('utf-8')
print(clean_text)