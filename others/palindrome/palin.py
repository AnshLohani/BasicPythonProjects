#Python program to check if a number is Palindrome or not.
#Palindrome numbers: Numbers which are exactly the same when reversed. Example: 121 , 234432 . If we reverse these numbers, we get the same numbers!


def checkPalindrome(number):
    number_string = str(number)
    if number_string == number_string[-1::-1]:
        print("The number given is a palindrome...")
    else:
        print("The number given is not palindrome...")

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("Thanks for using the program!")
        break
    elif len(number) == 1:
        print("Invaild Choice!")
    else:
        checkPalindrome(number)
        print("Enter 0 to Exit.")