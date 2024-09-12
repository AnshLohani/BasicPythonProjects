import random 



def number():
    num = list()
    temp = ""
    x = random.randint(1,9)
    num.append(x)
    for i in range(3):
        n = random.randint(0,9)
        num.append(n)
    for i in num:
        temp += f'{i}'

    return num
    

def displaylist(a):
    x = ''
    for i in a:
        x += f'{i}'
    print(x)


num = number()

'''

num = [1,2,3,4]

'''



word = ''
gl = list()
while True:
    if word == num:
        print("You won! Thanks for playing!")
        ch = input("Wanna play again? (y/n): ")
        if ch.lower() == 'n':
            print("Thanks for playing!")
            break 
        else:
            num,wnum = number()
            word = ''
    guess = (input("Enter a four digit number: "))
    if guess.isalnum()==False:
        print("Not a valid choice! Try again!")
        continue
    
    else:
        l = list()
        t = ''
        for i in guess:
            l.append(int(i))

        for x in range(4):
            if num[x] == l[x]:
                gl.insert(x,num[x])
                t += f'{num[x]}'
            else:
                gl.insert(x,"X")
                t += 'x'
            word = t
    print(word)
 #      displaylist(gl)

                
        
        
    
          
        


          
