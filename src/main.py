import nltk   
from bs4 import *
from urllib import urlopen


url = "http://en.wikipedia.org/wiki/Bradford"
html = urlopen(url).read()
raw = BeautifulSoup(html)
clean_text = nltk.clean_url(url)
print(clean_text)