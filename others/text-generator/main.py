import random 

def text(wordsnum,wordrangemin,wordrangemax):
    mainstr = str()
    for x in range(wordsnum+1):
        tempstr = str()
        n = random.randrange(wordrangemin,wordrangemax+1)
        for j in range(n):
            i = random.randrange(97,122)
            l = chr(i)
            tempstr+=l
        mainstr = mainstr + tempstr + " "
    
    print(mainstr)

wordsnum= int(input("Enter how many words do you want: "))
wordrangemin= int(input("Enter minimum word length: "))
wordrangemax= int(input("Enter maximum word length: "))

text(wordsnum,wordrangemin,wordrangemax)