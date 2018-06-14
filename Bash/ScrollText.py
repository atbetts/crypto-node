import showDisplay as sd
import time
def scroll(wordlist):

    displayword = ""
    i = 0;
    for word in wordlist:
        if i<4:
            while(len(word)<20):
                word=word+" "
            if len(word)>20:
                word = word[0:20]
            displayword = displayword + word
    sd.printDisplay(displayword)
