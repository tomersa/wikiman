import sys
import wikipedia

if __name__ == "__main__":
    if len(sys.argv) < 2:
	print "Usage: wiki [search term]"
	sys.exit(0)
    
    name_arg = " ".join(sys.argv[1:])
    search_term = wikipedia.search(name_arg)[0]  # Using first result as search

    print u"Searching for: {0}".format(search_term)

    wiki_page = wikipedia.page(search_term)

    print u"Title: {0}".format(wiki_page.title)
    print u"\n"
    print wiki_page.content.encode('utf-8')
    print u"Based on url: {0}".format(wiki_page.url)

# >>> wiki_page.links[0]
# # u'1790 United States Census'

# >>> wikipedia.set_lang("fr")
# >>> wikipedia.summary("Facebook", sentences=1)
# # Facebook est un service de
