import sys
import wikipedia
import codecs

if __name__ == "__main__":
    name_arg = codecs.encode(sys.argv[1])
    search_term = codecs.encode(wikipedia.search(name_arg)[0]) #Using first result as search

    print u"Searching for: {0}".format(search_term)

    wiki_page = wikipedia.page(search_term)

    print u"Title: {0}".format(wiki_page.title)
    print u"\n\n"
    print codecs.encode(wiki_page.content, 'utf-8')
    print u"Based on url: {0}".format(wiki_page.url)

# >>> wiki_page.links[0]
# # u'1790 United States Census'

# >>> wikipedia.set_lang("fr")
# >>> wikipedia.summary("Facebook", sentences=1)
# # Facebook est un service de