import random


def number():
    num = list()
    x = random.randint(1,9)
    num.append(f"{x}")
    for i in range(3):
        n = random.randint(0,9)
        num.append(f"{n}")
    return num


def display(d):
    xi = d.values()
    j = ""
    for i in xi:
        j += f"{i}"
    print(j)


x = number()
d = {0:'X',1:'X',2:'X',3:'X'}


while True:

    if 'X' not in d.values():
        print("You won! Thanks for playing!")
        ch = input("Wanna play again? (y/n): ")
        if ch.lower() == 'n':
            print("Thanks for playing!")
            break 
        else:
            x = number()
            d = {0:'X',1:'X',2:'X',3:'X'}
        

    guess = input("Enter a four digit guess:")

    temp = list()
    for i in guess:
        temp.append(i)
  
    for i in range(len(x)):
        if x[i] == temp[i]:
            d[i] = x[i]
        else:
            continue
    display(d)
