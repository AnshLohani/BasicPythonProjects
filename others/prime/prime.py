#Function to detect if a number is prime
#A prime number is a number which only has 2 factors(only divisible by 2 numbers) i.e 1 and the number itself
'''In this function we check is a given number (num) can be divisible by any of the numbers starting from 2 to the number prior to num.
This ensures that if there is one number which can divide num then num will be considered not prime.
But if there is'nt any number that satisfy our logic then the number num is considered a Prime Number and will be printed in the following code.'''

def prime(num):
  for i in range(2,num):
    if a%i == 0:
      print('Not Prime')
      break
  else:
    print('Prime')


num= int(input("Enter a number: "))
prime(num)