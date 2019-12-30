# Read text from a document
# Check text from cursed words
import urllib.request as url

def read_text():
    quotes = open('movie_quotes.txt')
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    chk_profanity(contents_of_file)

def chk_profanity(text):
    connection = url.urlopen("https://http://www.wdylike.appspot.com/?q={0}".format(text))
    output = connection.read()
    print(output)
    connection.close()
    # if True in output:
    #     print("Prpfanity Alert!!")
    # elif False in output:
    #     print("Thid document has no curse words!")
    # else:
    #     print("Could not scan the document properly")

read_text()