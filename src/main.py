import sys
import wikipedia

if __name__ == "__main__":
    name_arg = sys.argv[1]
    search_term = wikipedia.search(name_arg)[0]  # Using first result as search
    # output = []

    print u"Searching for: {0}".format(search_term)

    wiki_page = wikipedia.page(search_term)

    print u"Title: {0}".format(wiki_page.title)
    print u"\n"
    print wiki_page.content.encode('utf-8')
    print u"Based on url: {0}".format(wiki_page.url)

    #output_string = u""
    #for i in output:
        #output_string = output_string + i

    #output_string = output_string

    #less_pipe = Popen(['less'], stdin=subprocess.PIPE)
    #less_pipe.stdin.write(output_string)
    # for i in output:
				# print i
    #for i in output:
				#print i


# >>> wiki_page.links[0]
# # u'1790 United States Census'

# >>> wikipedia.set_lang("fr")
# >>> wikipedia.summary("Facebook", sentences=1)
# # Facebook est un service de