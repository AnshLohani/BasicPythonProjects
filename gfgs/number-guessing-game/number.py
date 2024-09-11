import random 

scores = list()
def newn():
    num = random.randint(0,100)
    return num
num = newn()
gn = 1
while True:
    guess = int(input("Enter you guess: (Any number between 0-100) "))

    if guess<num:
        print("You guessed too low!")
        gn += 1
    elif guess>num:
        print("You guessed too high!")
        gn += 1
    else:
        print("You guessed correct!")
        if len(scores) == 0:
            pgn = gn
            print(f"Your new highscore: {pgn}")
            scores.append(gn)
        else:
            scores.append(gn)
            pgn = min(scores)
            print(f"Score: {gn}")
            print(f"Your highscore: {pgn}")                
        gn=0
    
        ch = input("Play more? (y/n): ")
        if ch.lower() == "n":
            print(f"Your highscore: {pgn}") 
            break
        else:
            num = newn()
            continue        