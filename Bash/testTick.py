import ScrollText
import time
i=0
word = '0-1-2-3-4-5-6-7-8-9-10-11-12-13-14-15'
j = 20
while(True):
    if(i>j):
        wordlist = ['1','123','123456',word[i:]+word[0:j]]
        ScrollText.scroll(wordlist)
    else:
        wordlist = ['1','123','123456',word[i:j]]
        ScrollText.scroll(wordlist)

    
    i=i+1
    j=j+1
    if(i>len(word)):
            i=0
    if(j>len(word)):
            j=1
    time.sleep(.01666)
