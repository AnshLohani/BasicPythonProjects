import random 
import time

while True:
    print("Welcome to the Rock - Paper - Scissor Game!")
    print('''Pick one of 
          Rock (0)
          Paper (1)
          Scissors (2)  
          ''')
    d = {0:"Rock",1:"Paper",2:"Scissors"}
    ch = int(input("Enter your choice: "))
    if ch > 2 or ch < 0:
        print("Invalid Choice! Retry")
        continue
    else:
        print(f"User's Choice: {d[ch]}")
        compchoice = random.randint(0,2)
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        time.sleep(1)
        print('.')
        print(f"Computer's Choice: {d[compchoice]}")
        if ch == 0:
            if compchoice == 0:
                print("Thats a Tie!")
            elif compchoice == 1:
                print("You Win!")
            else:
                print("You Lose!")
        elif ch == 1:
            if compchoice == 0:
                print("You Win!")
            elif compchoice == 1:
                print("Thats a Tie!")
            else:
                print("You Lose!")
        else:
            if compchoice == 0:
                print("You Lose!")
            elif compchoice == 1:
                print("You Win!")
            else:
                print("Thats a tie!")
    c = input("Want to play again? (y/n): ")
    if c.lower() == 'n':
        break
    else:
        continue