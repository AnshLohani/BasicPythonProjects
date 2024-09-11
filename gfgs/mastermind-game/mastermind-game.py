import random 



def number():
    num = list()
    x = random.randint(1,9)
    num.append(x)
    for i in range(3):
        n = random.randint(0,9)
        num.append(n)
    return num
    

num = number()

word = ''
wordl = list()
while True:
    guess = input("Enter a four digit number: ")
    if guess.isnumeric() == True:
        if int(guess) < 9999 or int(guess) > 1000:
            for i in range(len(guess)):
                if guess[i] == num[i]:
                    word += f" {guess[i]} "
                    wordl.append(guess[i])
                else:
                    word += " X "
                    wordl.append('X')

                
       
    else:
        print("invalid choice! Retry")
        pass

          
