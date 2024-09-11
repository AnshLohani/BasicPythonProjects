import random 

num = 0

def botchance():
    # x --> the places that the bot moves (consecutive numbers)
    x = random.randint(1,3)
    return x 

def userchance():
    ch = int(input("Enter numbers you want to add (0-3): "))
    if ch not in [1,2,3]:
        userchance()
    else:
        return ch

def game():
    x = list()
    for i in range(1,num+1):
        x.append(i)
    return x



while True:
    start = int(input("Enter who starts (0=user, 1=computer): "))
    if start == 1:
        num += botchance()
        print(f"Bot's Chance: {game()}")
        while num<21:
            num+=userchance()
            if num>=21:
                print("You Lost!")
                break
            print(f"User's Chance: {game()}")
            num+=botchance()
            if num>=21:
                print("Computer Lost!")
                break
            print(f"Bot's Chance: {game()}")
        
    else:
        num += userchance()
        print(f"User's Chance: {game()}")
        while num<21:
            num+=botchance()
            if num>=21:
                print("Computer Lost!")
                break
            print(f"Bot's Chance: {game()}")
            num+=userchance()
            if num>=21:
                print("You Lost!")
                break
            print(f"User's Chance: {game()}")
    num=0

    
    
