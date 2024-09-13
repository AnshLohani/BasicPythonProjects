import random 

def rword():
    sample = [1,2,3,4,5,6,7,8,9]
    code=''
    for i in range(4):
        x = random.sample(sample,1)[0]
        code += f'{x}'
        sample.remove(x)
    return code

code = rword()
#print(code)
t=0

while True:
    cows = 0
    bulls = 0
    guess = input("Enter a guess of 4 digit: ")
    if len(guess)>4 or len(guess)<4 or guess.isnumeric() == False:
        print("Invalid Guess! Try again")
        continue
    else:
        if guess == code:
            print("You guessed the code and won!")
            print(f"It took you {t+1} tries")
            ch = input("Want to play again? (y/n): ")
            if ch.lower() == 'n':
                print("Thanks for playing!")
                break
            else:
                code= rword()
                t=0
        for i in range(4):
            if code[i] == guess[i]:
                bulls +=1
            if guess[i] in code and code[i] != guess[i]:
                cows += 1
        print(f"Your guess: {guess}")
        print(f"Bulls: {bulls}   Cows: {cows}")