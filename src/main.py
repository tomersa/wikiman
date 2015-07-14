import sys
import wikipedia
import os


def main():
    if len(sys.argv) < 2:
        print "Usage: wiki [search term]"
        sys.exit(0)
    name_arg = " ".join(sys.argv[1:])
    possible_search_terms = wikipedia.search(name_arg)
    # If a page with exactly the same name is found. It will be the search term.
    #Else, the user will be asked to choose a search term.
    if name_arg in possible_search_terms:
        search_term = name_arg

    else:
        search_term = possible_search_terms[0]
    print u"Searching for: {0}".format(search_term)
    try:
        wiki_page = wikipedia.page(search_term)

    except wikipedia.exceptions.DisambiguationError, e:
        print u"Couldn't find the exact term \"{0}\".{1}These are the closest options available:{1}{2}".format(
            search_term, \
            os.linesep, \
            unicode("".join([option + os.linesep for option in e.options])))
        return

    print u"Title: {0}".format(wiki_page.title)
    print u"\n"
    print wiki_page.content.encode('utf-8')
    print u"Based on url: {0}".format(wiki_page.url)


if __name__ == "__main__":
    main()
